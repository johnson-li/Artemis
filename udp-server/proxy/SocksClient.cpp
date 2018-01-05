//
// Created by 李学兵 on 2018/1/5.
//

#include <netdb.h>
#include <iostream>
#include <vector>
#include <arpa/inet.h>
#include "SocksClient.h"

std::string USER_NAME = "johnson163";
std::string PASSWORD = "welcOme0!";

namespace socks5 {
    SocksClient::SocksClient(std::string _ip, std::string _port, std::string _target_ip, std::string _target_port) : ip(
            _ip), port(_port), targetIP(_target_ip), targetPort(_target_port) {
    }

    SocksClient::~SocksClient() {
        destroy();
    }

    int SocksClient::connect() {
        state = Connecting;
        int sfd, res;
        ssize_t received;
        struct addrinfo *server_addr, *rp;

        // Resolve server IP
        addrinfo hints;
        memset(&hints, 0, sizeof(hints));
        hints.ai_family = AF_INET;
        hints.ai_socktype = SOCK_STREAM;
        res = getaddrinfo(ip.c_str(), port.c_str(), &hints, &server_addr);
        if (res != 0) {
            fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(res));
            return 1;
        }

        // Connect to the server
        for (rp = server_addr; rp != nullptr; rp = rp->ai_next) {
            sfd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
            if (sfd == -1) {
                continue;
            }
            char host[INET_ADDRSTRLEN];
            getnameinfo(rp->ai_addr, rp->ai_addrlen, host, sizeof(host), nullptr, 0, NI_NUMERICHOST);
            if (::connect(sfd, rp->ai_addr, rp->ai_addrlen) != -1) {
                if (rp->ai_addr->sa_family == AF_INET) {
                    std::cout << "connected to host: " << host << ":"
                              << ntohs(((struct sockaddr_in *) rp->ai_addr)->sin_port) << std::endl;
                } else {
                    std::cout << "connected to host: " << host << ":"
                              << ntohs(((struct sockaddr_in6 *) rp->ai_addr)->sin6_port) << std::endl;
                }
            }
            break;
        }

        // Send hello message
        std::vector<uint8_t> buffer;
        buffer.push_back(0x05); // version
        buffer.push_back(0x02); // method count
        buffer.push_back(0x00); // first method
        buffer.push_back(0x02); // second method
        ::send(sfd, reinterpret_cast<const char *>(buffer.data()), buffer.size(), 0);

        // Receive hello message
        size_t BUFFER_SIZE = 512;
        char read_buffer[512];
        received = ::recv(sfd, read_buffer, BUFFER_SIZE, 0);
        if (received > 0) {
            switch (read_buffer[1]) {
                case 0x00:
                    break;
                case 0x02:
                    buffer.clear();
                    buffer.push_back(0x01);
                    buffer.push_back(static_cast<const unsigned char>(USER_NAME.length()));
                    for (char &c: USER_NAME) {
                        buffer.push_back(static_cast<const unsigned char>(c));
                    }
                    buffer.push_back(static_cast<const unsigned char>(PASSWORD.length()));
                    for (char &c: PASSWORD) {
                        buffer.push_back(static_cast<const unsigned char>(c));
                    }
                    ::send(sfd, reinterpret_cast<const char *>(buffer.data()), buffer.size(), 0);
                    received = ::recv(sfd, read_buffer, BUFFER_SIZE, 0);
                    if (received > 0) {
                        if (read_buffer[1] == 0) {
                            std::cout << "authenticated" << std::endl;
                        } else {
                            fprintf(stderr, "failed authenticate\n");
                            return -1;
                        }
                    } else {
                        fprintf(stderr, "failed to read from the server\n");
                        return -1;
                    }
                    break;
                default:
                    fprintf(stderr, "unsupported authentication method");
                    return -1;
            }
        } else {
            fprintf(stderr, "failed to read from the server\n");
            return -1;
        }

        buffer.clear();
        buffer.push_back(0x05); // version
        buffer.push_back(0x03); // UDP
        buffer.push_back(0x00); // must be 0x00 always
        buffer.push_back(0x03); // 0x01 for IPv4 or 0x03 for domain name
        buffer.push_back(static_cast<const unsigned char>(targetIP.length()));
        for (char c : targetIP) {
            buffer.push_back(static_cast<const unsigned char>(c));
        }
        int port_num = stoi(targetPort);
        buffer.push_back(static_cast<const unsigned char>((port_num >> 16) & 0xff));
        buffer.push_back(static_cast<const unsigned char>(port_num & 0xff));
        ::send(sfd, reinterpret_cast<const char *>(buffer.data()), buffer.size(), 0);

        received = ::recv(sfd, read_buffer, BUFFER_SIZE, 0);
        if (received > 0) {
            char status = read_buffer[1];
            if (status != 0) {
                fprintf(stderr, "connection request failed: %d\n", status);
                return -1;
            }
            char addr_type = read_buffer[3];
            int addr_int;
            int port_int;
            switch (addr_type) {
                case 0x01:
                    addr_int =
                            (((int) read_buffer[4] & 0xff) << 24) | (((int) read_buffer[5] & 0xff) << 16) |
                            (((int) read_buffer[6] & 0xff) << 8) | ((int) read_buffer[7] & 0xff);
                    port_int = ((int) read_buffer[8] << 8) | ((int) read_buffer[9]);
                    in_addr addr;
                    addr.s_addr = ntohl(addr_int);
                    char ip_src[100];
                    sprintf(ip_src, "%s", inet_ntoa(addr));
                    std::cout << "Server address: " << ip_src << ":" << port_int << std::endl;
                    socksIP = std::string(ip_src);
                    socksPort = port_int;
                    break;
                case 0x03:
                    std::cout << "Got domain name" << std::endl;
                    fprintf(stderr, "unsupported addr type");
                    return -1;
                case 0x04:
                    std::cout << "Got IPv6 address" << std::endl;
                    fprintf(stderr, "unsupported addr type");
                    return -1;
                default:
                    fprintf(stderr, "unrecognized addr type");
                    return -1;
            }
        } else {
            fprintf(stderr, "failed to read from the server\n");
            return -1;
        }
        return 0;
    }

    ssize_t SocksClient::send(const char *buffer, const size_t size) {
        memset(&relyAddr, '0', sizeof(relyAddr));
        relyAddr.sin_family = AF_INET;
        relyAddr.sin_port = htons(socksPort);
        inet_pton(AF_INET, socksIP.c_str(), &(relyAddr.sin_addr));
        int fd = socket(AF_INET, SOCK_DGRAM, 0);
        return ::send(fd, buffer, size, 0);
    }

    ssize_t SocksClient::recv(char *buffer, const size_t size) {
        return 0;
    }

    void SocksClient::destroy() {
        state = SocksState::Closed;
    }
}

int main() {
//    socks5::SocksClient client = socks5::SocksClient("162.210.198.8", "1510", "gcp.xuebing.name", "1500");
    socks5::SocksClient client = socks5::SocksClient("127.0.0.1", "1080", "gcp.xuebing.name", "1500");
    client.connect();
    client.send("123", 3);
    return 0;
}