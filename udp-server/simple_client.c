//
// Created by 李学兵 on 2018/1/1.
//
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/time.h>
#include <fcntl.h>
#include <unistd.h>


#define BUFSIZE 1024000
#define PORT 8081

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("too few arguments");
        return 1;
    } else if (argc > 2) {
        printf("too much arguments");
        return 1;
    }
    struct timeval start, end, dns_start, dns_end;
    ssize_t result;
    ssize_t recv;
    int server_fd;
    int router_fd;
    char server_buf[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a'};
    char read_buf[BUFSIZE];

    server_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_fd < 0)
        perror("ERROR opening socket");
    fcntl(server_fd, F_SETFL, O_NONBLOCK);
    char *server_ip = argv[1];
    struct sockaddr_in server_addr, local_addr;
    bzero((char *) &server_addr, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    gettimeofday(&start, NULL);
    if (server_ip[0] > '9' || server_ip[0] < '0') {
        struct hostent *he;
        gettimeofday(&dns_start, NULL);
        he = gethostbyname(server_ip);
        gettimeofday(&dns_end, NULL);
        printf("DNS delay %f ms\n",
               (double) (dns_end.tv_usec - dns_start.tv_usec) / 1000 + (dns_end.tv_sec - dns_start.tv_sec) * 1000);
        struct in_addr **addr_list;
        addr_list = (struct in_addr **) he->h_addr_list;
        server_addr.sin_addr = *addr_list[0];
    } else {
        inet_pton(AF_INET, server_ip, &(server_addr.sin_addr));
    }

    // Bind src port to 12345
    local_addr.sin_family = AF_INET;
    local_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    local_addr.sin_port = htons(12345);
    if (bind(server_fd, (struct sockaddr *) &local_addr, sizeof(local_addr)) < 0) {
        perror("Error occurred when binding to port: 12345");
    }

    socklen_t addrlen;
    recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr,
                    sizeof(server_addr));
    printf("sent %ld bytes to the server\n", result);

    for (;;) {
        recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
        gettimeofday(&end, NULL);
        double diff = (double) (end.tv_usec - start.tv_usec) / 1000 + (end.tv_sec - start.tv_sec) * 1000;
        if (recv != -1) {
            break;
        }
        if (diff > 5000) {
            return 1;
        }
    }
    printf("got %ld bytes from the server\n", recv);
    gettimeofday(&end, NULL);

    printf("cost %f ms\n", (double) (end.tv_usec - start.tv_usec) / 1000 + (end.tv_sec - start.tv_sec) * 1000);
    char name[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &(server_addr.sin_addr), name, INET_ADDRSTRLEN);
    printf("server ip by DNS %s\n", name);
    return 0;
}
