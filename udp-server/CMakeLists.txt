cmake_minimum_required(VERSION 3.9)
project(udp_server)

set(CMAKE_CXX_STANDARD 11)

add_executable(udp_server
        serviceid_server.cpp client.cpp)
