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

        enum SocksType {
            UDP, TCP
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
        SocksType type;
        int rfd, sfd;

    public:
        unsigned long long timeoutDuration = 8000;

        SocksClient(std::string _ip, std::string _port, std::string _target_ip, std::string _target_port,
                    SocksType _type);

        ~SocksClient();

        int connect();

        ssize_t sendTCP(const char *buffer, const size_t size);

        ssize_t sendUDP(const char *buffer, const size_t size);

        ssize_t send(const char *buffer, const size_t size) {
            switch (type) {
                case TCP:
                    return sendTCP(buffer, size);
                case UDP:
                    return sendUDP(buffer, size);
            }
        }

        ssize_t recv(char *buffer, const size_t size);

        void destroy();

        const SocksState &getState();
    };

}

#endif //UDP_SERVER_SOCKSCLIENT_H
