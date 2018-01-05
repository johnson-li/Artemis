//
// Created by 李学兵 on 2018/1/5.
//

#ifndef UDP_SERVER_SOCKSCLIENT_H
#define UDP_SERVER_SOCKSCLIENT_H


#include <string>

namespace socks5 {
    class SocksClient {
    public:
        enum SocksState {
            Open,
            Connecting,
            Closed
        };

        struct SocksUrl {
            enum Type {
                WS,
                WSS,
                HTTP
            };

            Type type;
            std::string ip;
            unsigned int port;
            uint8_t ipv4[4];
            uint8_t ipv6[16];
        };

    private:
        std::string ip;
        std::string port;
        std::string targetIP;
        std::string targetPort;
        SocksState state;
        std::string socksIP;
        int socksPort;
        sockaddr_in relyAddr;

    public:
        unsigned long long timeoutDuration = 8000;

        SocksClient(std::string _ip, std::string _port, std::string _target_ip, std::string _target_port);

        ~SocksClient();

        SocksClient::SocksUrl scanURL(const std::string _url);

        int connect();

        ssize_t send(const char *buffer, const size_t size);

        ssize_t recv(char *buffer, const size_t size);

        void destroy();

        const SocksState &getState();
    };

}

#endif //UDP_SERVER_SOCKSCLIENT_H
