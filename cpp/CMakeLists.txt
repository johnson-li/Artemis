cmake_minimum_required(VERSION 3.5)
project(cpp)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-lmysqlclient")

add_executable(demo src/demo/demo.cpp)
add_executable(balancer src/loadbalancer/balancer.cpp)
