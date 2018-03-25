//
// Created by 李学兵 on 2018/1/1.
//
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/time.h>

#define BUFSIZE 1024000
#define PORT 8081

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("too few arguments");
        printf("Usage: client router");
        return 1;
    } else if (argc > 2) {
        printf("too much arguments");
        printf("Usage: client router");
        return 1;
    }
    ssize_t result;
    ssize_t recv;
    struct timeval start, end, dns_start, dns_end;
    int router_fd;
    char router_buf[1200];
    char read_buf[BUFSIZE];
    struct sockaddr_in router_addr, local_addr2;
    socklen_t addrlen;
    char name[INET_ADDRSTRLEN];

    char *router_ip = argv[1];
    bzero((char *) &router_addr, sizeof(router_addr));
    router_addr.sin_family = AF_INET;
    router_addr.sin_port = htons(PORT);


    // Bind src port to 12345
    router_fd = socket(AF_INET, SOCK_DGRAM, 0);
    local_addr2.sin_family = AF_INET;
    local_addr2.sin_addr.s_addr = htonl(INADDR_ANY);
    local_addr2.sin_port = htons(12346);
    if (bind(router_fd, (struct sockaddr *) &local_addr2, sizeof(local_addr2)) < 0) {
        perror("Error occurred when binding router fd to port: 12346");
    }

    gettimeofday(&start, NULL);
    if (router_ip[0] > '9' || router_ip[0] < '0') {
        struct hostent *he;
        gettimeofday(&dns_start, NULL);
        he = gethostbyname(router_ip);
        gettimeofday(&dns_end, NULL);
        printf("DNS delay %f ms\n",
               (double) (dns_end.tv_usec - dns_start.tv_usec) / 1000 + (dns_end.tv_sec - dns_start.tv_sec) * 1000);
        struct in_addr **addr_list;
        addr_list = (struct in_addr **) he->h_addr_list;
        router_addr.sin_addr = *addr_list[0];
        inet_ntop(AF_INET, &(router_addr.sin_addr), name, INET_ADDRSTRLEN);
    } else {
        inet_pton(AF_INET, router_ip, &(router_addr.sin_addr));
    }

    result = sendto(router_fd, router_buf, sizeof(router_buf) / sizeof(router_buf[0]), 0,
                    (struct sockaddr *) &router_addr, sizeof(router_addr));
    printf("sent %zd bytes to the router\n", result);

    for (;;) {
        recv = recvfrom(router_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &router_addr, &addrlen);
        char str[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &(router_addr.sin_addr), str, INET_ADDRSTRLEN);
        printf("received %zd bytes from %s:%d\n", recv, str, ntohs(router_addr.sin_port));
        gettimeofday(&end, NULL);
        double diff = (double) (end.tv_usec - start.tv_usec) / 1000 + (end.tv_sec - start.tv_sec) * 1000;
        if (recv != -1) {
            break;
        }
        if (diff > 5000) {
            return 1;
        }
    }
    gettimeofday(&end, NULL);
    printf("got %zd bytes from the server\n", recv);
    printf("server ip by DNS %s\n", name);
    printf("cost %f ms\n", (double) (end.tv_usec - start.tv_usec) / 1000 + (end.tv_sec - start.tv_sec) * 1000);
    return 0;
}


