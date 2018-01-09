//
// Created by 李学兵 on 2018/1/1.
//
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <fcntl.h>
#include <time.h>
#include <unistd.h>

#define BUFSIZE 1024000
#define PORT 80

int main(int argc, char **argv) {
    if (argc < 3) {
        printf("too few arguments");
        printf("Usage: client router server");
        return 1;
    } else if (argc > 3) {
        printf("too much arguments");
        printf("Usage: client router server");
        return 1;
    }
    ssize_t result;
    ssize_t recv;
    clock_t start, end;
    int server_fd;
    int router_fd;
    char server_buf[] = {'i', 'n', 'i', 't'};
    char router_buf[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a'};
    char read_buf[BUFSIZE];

    char *router_ip = argv[1];
    char *server_ip = argv[2];
    struct sockaddr_in server_addr;
    struct sockaddr_in router_addr;
    bzero((char *) &server_addr, sizeof(server_addr));
    bzero((char *) &router_addr, sizeof(router_addr));
    server_addr.sin_family = AF_INET;
    router_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    router_addr.sin_port = htons(PORT);
    inet_pton(AF_INET, server_ip, &(server_addr.sin_addr));
    inet_pton(AF_INET, router_ip, &(router_addr.sin_addr));

    server_fd = socket(AF_INET, SOCK_DGRAM, 0);
    router_fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_fd < 0 || router_fd < 0)
        perror("ERROR opening socket");
    fcntl(server_fd, F_SETFL, O_NONBLOCK);

    socklen_t addrlen;
    recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr, sizeof(server_addr));
    printf("sent %ld bytes to the server\n", result);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr, sizeof(server_addr));
    printf("sent %ld bytes to the server\n", result);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr, sizeof(server_addr));
    printf("sent %ld bytes to the server\n", result);

    sleep(1);
    start = clock();
    result = sendto(router_fd, router_buf, sizeof(router_buf) / sizeof(router_buf[0]), 0,
                    (struct sockaddr *) &router_addr, sizeof(router_addr));
    printf("sent %ld bytes to the router\n", result);

    for (;;) {
        recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
        end = clock();
        double diff = (double) (end - start) / CLOCKS_PER_SEC;
        if (recv != -1) {
            break;
        }
        if (diff > 4) {
            return 1;
        }
    }
    printf("got %ld bytes from the server\n", recv);
    end = clock();

    printf("cost %f ms\n", (double) (end - start) / CLOCKS_PER_SEC * 1000);
    return 0;
}
