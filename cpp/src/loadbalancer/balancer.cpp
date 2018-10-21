//
// Created by 李学兵 on 2018/10/20.
//

#include <arpa/inet.h>
#include <linux/if_packet.h>
#include <linux/ip.h>
#include <linux/udp.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <mysql/mysql.h>
#include <mysql/my_global.h>
#include <net/if.h>
#include <netinet/ether.h>
#include <unistd.h>

#define DEFAULT_IF    "ens33"
#define BUF_SIZ       (1024 * 128)
#define ETHER_TYPE    0x0800

MYSQL *mysql_connect() {
    MYSQL *mysql = (MYSQL *) calloc(1, sizeof(MYSQL));
    mysql_init(mysql);
    mysql_real_connect(mysql, "127.0.0.1", "root", "root", "sid", 3306, NULL, 0);
    printf("Connected to data based");
    return mysql;
}

int main(int argc, char *argv[]) {
    char sender[INET_ADDRSTRLEN];
    int sockfd, ret, i;
    int sockopt;
    ssize_t numbytes;
    struct ifreq if_ip;    /* get ip addr */
    struct sockaddr_storage their_addr;
    uint8_t buf[BUF_SIZ];
    char ifName[IFNAMSIZ];

    /* Get interface name */
    if (argc > 1)
        strcpy(ifName, argv[1]);
    else
        strcpy(ifName, DEFAULT_IF);

    /* Header structures */
    struct ether_header *eh = (struct ether_header *) buf;
    struct iphdr *iph = (struct iphdr *) (buf + sizeof(struct ether_header));
    struct udphdr *udph = (struct udphdr *) (buf + sizeof(struct iphdr) + sizeof(struct ether_header));

    memset(&if_ip, 0, sizeof(struct ifreq));

    if ((sockfd = socket(PF_PACKET, SOCK_RAW, htons(ETHER_TYPE))) == -1) {
        perror("listener: socket");
        return -1;
    }

    if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &sockopt, sizeof sockopt) == -1) {
        perror("setsockopt");
        close(sockfd);
        exit(EXIT_FAILURE);
    }
    if (setsockopt(sockfd, SOL_SOCKET, SO_BINDTODEVICE, ifName, IFNAMSIZ - 1) == -1) {
        perror("SO_BINDTODEVICE");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    MYSQL *mysql = mysql_connect();

    while (1) {
        //printf("listener: Waiting to recvfrom...\n");
        numbytes = recvfrom(sockfd, buf, BUF_SIZ, 0, NULL, NULL);
        //printf("listener: got packet %lu bytes\n", numbytes);

        /* Get source IP */
        ((struct sockaddr_in *) &their_addr)->sin_addr.s_addr = iph->saddr;
        inet_ntop(AF_INET, &((struct sockaddr_in *) &their_addr)->sin_addr, sender, sizeof sender);

        /* Look up my device IP addr if possible */
        strncpy(if_ip.ifr_name, ifName, IFNAMSIZ - 1);
        if (ioctl(sockfd, SIOCGIFADDR, &if_ip) >= 0) { /* if we can't check then don't */
            //printf("Source IP: %s\n My IP: %s\n", sender, inet_ntoa(((struct sockaddr_in *)&if_ip.ifr_addr)->sin_addr));
            /* ignore if I sent it */
            if (strcmp(sender, inet_ntoa(((struct sockaddr_in *) &if_ip.ifr_addr)->sin_addr)) == 0) {
                //printf("but I sent it :(\n");
                ret = -1;
                continue;
            }
            if (iph->protocol != IPPROTO_UDP) {
                continue;
            }
            printf("udp dest: %d\n", udph->dest);
            if (udph->dest != htons(8080)) {
                continue;
            }
        }

        /* UDP payload length */
        ret = ntohs(udph->len) - sizeof(struct udphdr);

        /* Print packet */
        printf("\tData:");
        for (i = 0; i < numbytes; i++) printf("%02x:", buf[i]);
        printf("\n");

        /* forward to server */
        const char *opt;
        opt = "vxlan1";
        const int len = strnlen(opt, IFNAMSIZ);
        if (len == IFNAMSIZ) {
            fprintf(stderr, "Too long iface name");
            return 1;
        }
        int sd = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
        int on = 1;
        if (setsockopt(sd, SOL_SOCKET, SO_BINDTODEVICE, opt, len) == -1) {
            perror("setsockopt");
            close(sd);
            exit(EXIT_FAILURE);
        }
        if (setsockopt(sd, IPPROTO_IP, IP_HDRINCL, &on, sizeof(on)) == -1) {
            perror("setsockopt");
            close(sd);
            exit(EXIT_FAILURE);
        }
        struct sockaddr_in target;
        target.sin_family = AF_INET;
        target.sin_port = udph->dest;
        target.sin_addr.s_addr = iph->daddr;
        printf("length: %x, %ld\n", ntohs(iph->tot_len), sizeof(iph->tot_len));
        if (sendto(sd, iph, ntohs(iph->tot_len), MSG_DONTROUTE, (struct sockaddr *) &target, sizeof(target)) == -1) {
            perror("error forwarding packet");
            //return 1;
        }
    }
    close(sockfd);
    return ret;
}