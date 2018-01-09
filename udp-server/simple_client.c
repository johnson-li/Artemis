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
#include <time.h>


#define BUFSIZE 1024000
#define PORT 8080

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("too few arguments");
        return 1;
    } else if (argc > 2) {
        printf("too much arguments");
        return 1;
    }
    clock_t start, end, dns_start, dns_end;
    ssize_t result;
    ssize_t recv;
    int server_fd;
    int router_fd;
    char server_buf[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a'};
    char read_buf[BUFSIZE];

    server_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_fd < 0)
        perror("ERROR opening socket");
    char *server_ip = argv[1];
    struct sockaddr_in server_addr;
    bzero((char *) &server_addr, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    start = clock();
    if (server_ip[0] > '9' || server_ip[0] < '0') {
        struct hostent *he;
        dns_start = clock();
        he = gethostbyname(server_ip);
        dns_end = clock();
        printf("DNS delay %f ns\n", (double) (dns_end - dns_start) / CLOCKS_PER_SEC * 1000);
        struct in_addr **addr_list;
        addr_list = (struct in_addr **) he->h_addr_list;
        server_addr.sin_addr = *addr_list[0];
    } else {
        inet_pton(AF_INET, server_ip, &(server_addr.sin_addr));
    }

    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0, (struct sockaddr *) &server_addr,
                    sizeof(server_addr));
    printf("sent %ld bytes to the server\n", result);

    socklen_t addrlen;
    recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
    printf("got %ld bytes from the server\n", recv);
    end = clock();

    printf("cost %f ms\n", (double) (end - start) / CLOCKS_PER_SEC * 1000);
    char name[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &(server_addr.sin_addr), name, INET_ADDRSTRLEN);
    printf("server ip by DNS %s\n", name);
    return 0;
}