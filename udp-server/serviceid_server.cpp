#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <map>


#define PORT 80
#define BUFSIZE 1024000

int main(int argc, char **argv) {
    struct sockaddr_in sa_gre;
    struct sockaddr_in myaddr;      /* our address */
    struct sockaddr_in remaddr;     /* remote address */
    std::map<in_addr_t, sockaddr_in> map;
    socklen_t addrlen = sizeof(remaddr);            /* length of addresses */
    int recvlen;                    /* # bytes received */
    int result;
    int fd;                         /* our socket */
    unsigned char buf[BUFSIZE];     /* receive buffer */
    unsigned char send_buf[] = {'a', 'b', 'c'};     /* receive buffer */
    inet_pton(AF_INET, "10.10.10.10", &(sa_gre.sin_addr));

    /* create a UDP socket */
    if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("cannot create socket\n");
        return 0;
    }

    /* bind the socket to any valid IP address and a specific port */
    memset((char *) &myaddr, 0, sizeof(myaddr));
    myaddr.sin_family = AF_INET;
    myaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    myaddr.sin_port = htons(PORT);

    if (bind(fd, (struct sockaddr *) &myaddr, sizeof(myaddr)) < 0) {
        perror("bind failed");
        return 0;
    }

    /* now loop, receiving data and printing what we received */
    for (;;) {
        printf("waiting on port %d\n", PORT);
        recvlen = recvfrom(fd, buf, BUFSIZE, 0, (struct sockaddr *) &remaddr, &addrlen);
        char str[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &(remaddr.sin_addr), str, INET_ADDRSTRLEN);
        printf("received %d bytes from %s:%d\n", recvlen, str, remaddr.sin_port);
        if (recvlen > 10) {
            printf("got message from gre\n");
            sockaddr_in remaddr_old = map[remaddr.sin_addr.s_addr];
            inet_ntop(AF_INET, &(remaddr_old.sin_addr), str, INET_ADDRSTRLEN);
            result = sendto(fd, send_buf, sizeof(send_buf) / sizeof(send_buf[0]), 0, (struct sockaddr *) &remaddr_old,
                            sizeof(remaddr_old));
            printf("%d bytes sent to %s:%d\n", result, str, remaddr_old.sin_port);
        } else {
            printf("got message from internet\n");
            map[remaddr.sin_addr.s_addr] = remaddr;
        }
    }
}