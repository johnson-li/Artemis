#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include "uthash.h"
#include <net/if.h>


#define PORT 80
#define BUFSIZE 1024000

struct map_entry {
    in_addr_t key;
    struct sockaddr_in val;
    UT_hash_handle hh;
};

int main(int argc, char **argv) {
    struct map_entry *map = NULL;
    struct sockaddr_in sa_gre;
    struct sockaddr_in myaddr;      /* our address */
    struct sockaddr_in remaddr;     /* remote address */
    socklen_t addrlen = sizeof(remaddr);            /* length of addresses */
    ssize_t recvlen;                    /* # bytes received */
    ssize_t result;
    int fd;                         /* our socket */
    unsigned char buf[BUFSIZE];     /* receive buffer */
    unsigned char send_buf[] = {'a', 'b', 'c'};     /* receive buffer */
    inet_pton(AF_INET, "10.10.10.10", &(sa_gre.sin_addr));
    struct ifreq ifr;

    /* create a UDP socket */
    if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("cannot create socket\n");
        return 0;
    }

    memset(&ifr, 0, sizeof(ifr));
    snprintf(ifr.ifr_name, sizeof(ifr.ifr_name), "br1");
    if (setsockopt(fd, SOL_SOCKET, SO_BINDTODEVICE, (void *)&ifr, sizeof(ifr)) < 0) {
        perror("bind to interface failed\n");
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
        printf("received %ld bytes from %s:%d\n", recvlen, str, remaddr.sin_port);
        if (recvlen > 10) {
            printf("got message from gre\n");
            struct sockaddr_in remaddr_old;
            struct map_entry *entry;
            HASH_FIND_INT(map, &(remaddr.sin_addr.s_addr), entry);
            remaddr_old = entry->val;
            inet_ntop(AF_INET, &(remaddr_old.sin_addr), str, INET_ADDRSTRLEN);
            result = sendto(fd, send_buf, sizeof(send_buf) / sizeof(send_buf[0]), 0, (struct sockaddr *) &remaddr_old,
                            sizeof(remaddr_old));
            printf("%ld bytes sent to %s:%d\n", result, str, remaddr_old.sin_port);
        } else {
            printf("got message from internet\n");
            struct map_entry *entry;
            HASH_FIND_INT(map, &(remaddr.sin_addr.s_addr), entry);
            if (entry != NULL) {
                entry->val = remaddr;
            } else {
                entry = malloc(sizeof(struct map_entry));
                entry->key = remaddr.sin_addr.s_addr;
                entry->val = remaddr;
                HASH_ADD_INT(map, key, entry);
            }
        }
    }
}
