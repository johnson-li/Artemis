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
#include <net/if.h>
#include <netinet/ether.h>
#include <unistd.h>

#define BUF_SIZ       (1024 * 128)
#define ETHER_TYPE    0x0800

char *interfaceName;

//MYSQL *mysql_connect() {
//    MYSQL *mysql = (MYSQL *) calloc(1, sizeof(MYSQL));
//    mysql_init(mysql);
//    mysql_real_connect(mysql, "127.0.0.1", "root", "root", "sid", 3306, NULL, 0);
//    printf("Connected to data based");
//    return mysql;
//}


int init_socket() {
  int client_socket;
  int socket_opt = 1;
  char ifName[IFNAMSIZ];
  strcpy(ifName, interfaceName);
  if ((client_socket = socket(PF_PACKET, SOCK_RAW, htons(ETHER_TYPE))) == -1) {
    perror("failed to create socket for the client");
    return -1;
  }
  if (setsockopt(client_socket, SOL_SOCKET, SO_REUSEADDR, &socket_opt, sizeof socket_opt) == -1) {
    perror("failed to set reuse address");
    close(client_socket);
    return -1;
  }
  if (setsockopt(client_socket, SOL_SOCKET, SO_BINDTODEVICE, ifName, IFNAMSIZ - 1) == -1) {
    perror("failed to bind to interface");
    close(client_socket);
    return -1;
  }
  return client_socket;
}

void forwarding() {

}

//void parse_initial_packet() {
//    uint8_t *content = quic + 13;
//}

void listen_socket(int client_socket) {
//  printf("listen\n");
  char ifName[IFNAMSIZ];
  strcpy(ifName, interfaceName);
  uint8_t buf[BUF_SIZ];
  struct ether_header *eh = (struct ether_header *) buf;
  struct iphdr *iph = (struct iphdr *) (buf + sizeof(struct ether_header));
  struct udphdr *udph = (struct udphdr *) (buf + sizeof(struct iphdr) + sizeof(struct ether_header));
  uint8_t *quic = buf + sizeof(udphdr) + sizeof(struct iphdr) + sizeof(ether_header);
  struct ifreq if_ip;
  memset(&if_ip, 0, sizeof(struct ifreq));
  struct sockaddr_storage client_addr;
  char sender_ip[INET_ADDRSTRLEN];
  ssize_t bytes = recvfrom(client_socket, buf, BUF_SIZ, 0, NULL, NULL);

  ((struct sockaddr_in *) &client_addr)->sin_addr.s_addr = iph->saddr;
  inet_ntop(AF_INET, &((struct sockaddr_in *) &client_addr)->sin_addr, sender_ip, sizeof sender_ip);

  strncpy(if_ip.ifr_name, ifName, IFNAMSIZ - 1);
  if (ioctl(client_socket, SIOCGIFADDR, &if_ip) >= 0) {
    if (strcmp(sender_ip, inet_ntoa(((struct sockaddr_in *) &if_ip.ifr_addr)->sin_addr)) == 0) {
      return;
    }
    if (iph->protocol != IPPROTO_UDP) {
      return;
    }
    if (udph->dest != htons(4433)) {
      return;
    }
  } else {
    perror("failed to get local address");
    return;
  }
  int udp_size = ntohs(udph->len) - sizeof(struct udphdr);
  printf("got %lu(%d) bytes from %s\n", bytes, udp_size, sender_ip);
  forwarding();
}

int main(int argc, char *argv[]) {
  interfaceName = argv[1];
  if (argc < 2) {
    printf("Usage: balancer interfaceName\n");
    return -1;
  }
  printf("Running balancer ...\n");
  int socket = init_socket();
  for (;;) {
    listen_socket(socket);
  }
}