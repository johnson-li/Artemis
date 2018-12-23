#!/usr/bin/env bash
#remote='johnson@172.16.156.102'
remote='workstation-br'
scp -r /Users/johnson/Workspace/Hestia/cpp/src ${remote}:~/Workspace/Hestia/cpp
scp -r /Users/johnson/Workspace/Hestia/cpp/CMakeLists.txt ${remote}:~/Workspace/Hestia/cpp
scp -r /Users/johnson/Workspace/Hestia/cpp/compile.sh ${remote}:~/Workspace/Hestia/cpp
