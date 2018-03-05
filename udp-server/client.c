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
#include <sys/time.h>
#include <unistd.h>

#define BUFSIZE 1024000
#define PORT 8081

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
    struct timeval start, end;
    int server_fd;
    int router_fd;
    char server_buf[] = {'i', 'n', 'i', 't'};
    char router_buf[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a'};
    char read_buf[BUFSIZE];

    char *router_ip = argv[1];
    char *server_ip = argv[2];
    struct sockaddr_in server_addr, router_addr, local_addr1, local_addr2;
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


    // Bind src port to 12345
    local_addr1.sin_family = AF_INET;
    local_addr1.sin_addr.s_addr = htonl(INADDR_ANY);
    local_addr1.sin_port = htons(12345);
    if (bind(server_fd, (struct sockaddr *) &local_addr1, sizeof(local_addr1)) < 0) {
        perror("Error occurred when binding server fd to port: 12345");
    }
    // Bind src port to 12345
    local_addr2.sin_family = AF_INET;
    local_addr2.sin_addr.s_addr = htonl(INADDR_ANY);
    local_addr2.sin_port = htons(12346);
    if (bind(router_fd, (struct sockaddr *) &local_addr2, sizeof(local_addr2)) < 0) {
        perror("Error occurred when binding router fd to port: 12346");
    }

    socklen_t addrlen;
    recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr, sizeof(server_addr));
    printf("sent %zd bytes to the server\n", result);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr, sizeof(server_addr));
    printf("sent %zd bytes to the server\n", result);
    result = sendto(server_fd, server_buf, sizeof(server_buf) / sizeof(server_buf[0]), 0,
                    (struct sockaddr *) &server_addr, sizeof(server_addr));
    printf("sent %zd bytes to the server\n", result);

    sleep(1);

    do {
        recv = recvfrom(server_fd, read_buf, BUFSIZE, 0, (struct sockaddr *) &server_addr, &addrlen);
    } while (recv > 0);

    gettimeofday(&start, NULL);
    result = sendto(router_fd, router_buf, sizeof(router_buf) / sizeof(router_buf[0]), 0,
                    (struct sockaddr *) &router_addr, sizeof(router_addr));
    printf("sent %zd bytes to the router\n", result);

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
    printf("got %zd bytes from the server\n", recv);
    gettimeofday(&end, NULL);

    printf("cost %f ms\n", (double) (end.tv_usec - start.tv_usec) / 1000 + (end.tv_sec - start.tv_sec) * 1000);
    return 0;
}
