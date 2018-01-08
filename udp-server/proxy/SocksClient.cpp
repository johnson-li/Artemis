//
// Created by 李学兵 on 2018/1/5.
//

#include <netdb.h>
#include <iostream>
#include <vector>
#include <arpa/inet.h>
#include <thread>
#include "SocksClient.h"

std::string USER_NAME = "johnson163";
std::string PASSWORD = "welcOme0!";

namespace socks5 {
    SocksClient::SocksClient(std::string _ip, std::string _port, std::string _target_ip, std::string _target_port,
                             SocksType _type) : ip(_ip), port(_port), targetIP(_target_ip), targetPort(_target_port),
                                                type(_type) {
    }

    SocksClient::~SocksClient() {
        destroy();
    }

    int SocksClient::connect() {
        state = Connecting;
        int res;
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
        std::cout << "send hello message" << std::endl;
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
                    std::cout << "send authentication message" << std::endl;
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
        switch (type) {
            case UDP:
                buffer.push_back(0x03);
                break;
            case TCP:
                buffer.push_back(0x01);
                break;
        }
        buffer.push_back(0x00); // must be 0x00 always
        buffer.push_back(0x01); // 0x01 for IPv4 or 0x03 for domain name
//        buffer.push_back(static_cast<const unsigned char>(targetIP.length()));
//        for (char c : targetIP) {
//            buffer.push_back(static_cast<const unsigned char>(c));
//        }
//        for (int i = 0; i < 4; i++) {
//            buffer.push_back(0x00);
//        }
//        int port_num = stoi(targetPort);
        buffer.push_back(35);
        buffer.push_back(193);
        buffer.push_back(107);
        buffer.push_back(149);
        int port_num = 1500;
        buffer.push_back(static_cast<const unsigned char>((port_num >> 8) & 0xff));
        buffer.push_back(static_cast<const unsigned char>(port_num & 0xff));
        std::cout << "send request message" << std::endl;
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
                    port_int = (((int) read_buffer[8] & 0xff) << 8) | (((int) read_buffer[9]) & 0xff);
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
            fprintf(stderr, "failed to read from the server: %ld\n", received);
            return -1;
        }
        memset(&relyAddr, 0, sizeof(relyAddr));
        relyAddr.sin_family = AF_INET;
        relyAddr.sin_port = htons(socksPort);
        inet_pton(AF_INET, socksIP.c_str(), &(relyAddr.sin_addr));
        switch (type) {
            case UDP:
                rfd = socket(AF_INET, SOCK_DGRAM, 0);
                break;
            case TCP:
                rfd = socket(AF_INET, SOCK_STREAM, 0);
                break;
        }
//        if (::connect(rfd, (struct sockaddr *) &relyAddr, sizeof(relyAddr)) == -1) {
//            fprintf(stderr, "failed to connect");
//            return -1;
//        }
        sockaddr_in src_addr;
        memset(&src_addr, 0, sizeof(src_addr));
        src_addr.sin_family = AF_INET;
        src_addr.sin_addr.s_addr = htonl(INADDR_ANY);
        src_addr.sin_port = htons(12345);
        if ((received = ::bind(rfd, (sockaddr *) &src_addr, sizeof(src_addr))) < 0) {
            fprintf(stderr, "failed to bind: %ld\n", received);
            return -1;
        }
        return 0;
    }

    ssize_t SocksClient::sendTCP(const char *buffer, const size_t size) {
//        return ::send(rfd, buffer, size, 0);
        return ::send(sfd, buffer, size, 0);
    }

    ssize_t SocksClient::sendUDP(const char *buffer, const size_t size) {
        std::vector<uint8_t> send_buffer;
        send_buffer.push_back(0x00);
        send_buffer.push_back(0x00);
        send_buffer.push_back(0x00);
        send_buffer.push_back(0x01);
//        send_buffer.push_back(static_cast<unsigned char>(targetIP.length()));
//        for (char c: targetIP) {
//            send_buffer.push_back(c);
//        }
        // 35.193.107.149
        send_buffer.push_back(35);
        send_buffer.push_back(193);
        send_buffer.push_back(107);
        send_buffer.push_back(149);
        int port_num = stoi(targetPort);
        send_buffer.push_back(static_cast<const unsigned char>((port_num >> 8) & 0xff));
        send_buffer.push_back(static_cast<const unsigned char>(port_num & 0xff));

        for (int i = 0; i < size; i++) {
            send_buffer.push_back(buffer[i]);
        }
        return ::sendto(rfd, send_buffer.data(), send_buffer.size(), 0, (sockaddr *) &relyAddr, sizeof(relyAddr));
    }


    ssize_t SocksClient::recv(char *buffer, const size_t size) {
        return 0;
    }

    void SocksClient::destroy() {
        state = SocksState::Closed;
    }
}

int main() {
//    socks5::SocksClient client = socks5::SocksClient("104.151.241.187", "10925", "gcp.xuebing.name", "1500",
//                                                     socks5::SocksClient::SocksType::TCP);
    socks5::SocksClient client = socks5::SocksClient("162.210.198.8", "1200", "gcp.xuebing.name", "1500",
                                                     socks5::SocksClient::SocksType::TCP);
//    socks5::SocksClient client = socks5::SocksClient("111.230.113.142", "1080", "gcp.xuebing.name", "1500",
//                                                     socks5::SocksClient::SocksType::UDP);
//    socks5::SocksClient client = socks5::SocksClient("127.0.0.1", "5555", "gcp.xuebing.name", "1500");
    client.connect();
    client.send("123", 3);
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return 0;
}