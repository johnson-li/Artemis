Simulation Testbed
===

Please follow the following instructions to run the programme. 
It has been verified on a 64-bit Ubuntu 18.04 system.
Please be careful on each step. 
Check the error if something exceptional happens.

Prerequisite
===
```bash
sudo apt install -y libev-dev, libmysqlclient-dev, vagrant
```

Get the code
===
Suppose that the working directory is ~/Workspace

```bash
git clone --depth 1 -b quic https://github.com/tatsuhiro-t/openssl
git clone -b loadbalancer git@github.com:johnson-li/ngtcp2.git
git clone git@github.com:johnson-li/Hestia.git
```

Compile the code
===
```bash
cd ~/Workspace/openssl/
./config enable-tls1_3 --prefix=$PWD/build
make -j$(nproc)
make install_sw
cd ~/Workspace/ngtcp2/
./configure PKG_CONFIG_PATH=$PWD/../openssl/build/lib/pkgconfig LDFLAGS="-Wl,-rpath,$PWD/../openssl/build/lib"
make -j$(nproc)
```

Run the experiment
===
```bash
# destroy is set only at the first time to initiate virtual machines. 
destroy=1 ~/Workspace/Hestia/experiment/run-experiment.sh
```

The script will create several virtual machines and run the experiment automatically.
