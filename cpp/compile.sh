#!/usr/bin/env bash

cmake -DCMAKE_BUILD_TYPE=Debug -G "CodeBlocks - Unix Makefiles" .
cmake --build . --target balancer -- -j 4
