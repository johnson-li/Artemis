cmake_minimum_required(VERSION 3.9)
project(udp_server)

set(CMAKE_CXX_STANDARD 11)

add_executable(udp_server
        serviceid_server.c client.c proxy/SocksClient.cpp proxy/SocksClient.h simple_client.c)

add_executable(demo
        demo.c)

add_executable(raw_socket
        raw_socket.c)