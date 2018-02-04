import os

from fabric.api import *

env.warn_only = True
env.skip_bad_hosts = True
env.use_ssh_config = True
env.ssh_config_path = os.path.dirname(os.path.dirname(__file__)) + '/resources/ssh/config_planetlab'

env.hosts = ['planetlab13.net.in.tum.de', 'planetlab1.informatik.uni-goettingen.de', 'planetlab1.upm.ro',
             'planetlab2.informatik.uni-goettingen.de', 'planetlab-2.cs.ucy.ac.cy', 'planet4.cs.huji.ac.il',
             'netissime2.planet-lab.eu', 'puri.mimuw.edu.pl', 'planetlab2.upm.ro', 'planetlab-2.ing.unimo.it',
             'vicky.planetlab.ntua.gr', 'planetlab1.cs.uit.no', 'dplanet1.uoc.edu',
             'planetvs2.informatik.uni-stuttgart.de', 'planetlab11.net.in.tum.de',
             'planet-lab-node2.netgroup.uniroma2.it', 'kulcha.mimuw.edu.pl', 'planet3.cs.huji.ac.il',
             'stella.planetlab.ntua.gr', 'ple44.planet-lab.eu', 'onelab2.pl.sophia.inria.fr', 'ple1.planet-lab.eu',
             'aladdin.planetlab.extranet.uni-passau.de', 'netissime1.planet-lab.eu', 'ple1.cesnet.cz',
             'ple42.planet-lab.eu', 'ple43.planet-lab.eu', 'ple41.planet-lab.eu', 'planetlab3.cs.uoregon.edu',
             'planetlab3.eecs.umich.edu', 'planetlab1.utdallas.edu', 'planetlab1.cs.purdue.edu',
             'planetlab-n1.wand.net.nz', 'planetlab3.cesnet.cz', 'planetlab-1.scie.uestc.edu.cn',
             'planetlab-js1.cert.org.cn', 'planetlab1.temple.edu', 'saturn.planetlab.carleton.ca', 'planetlab1.unr.edu',
             'planet-lab4.uba.ar', 'planetlab3.rutgers.edu', 'planetlab1.pop-pa.rnp.br', 'planetlab2.pop-pa.rnp.br',
             'pl2.eng.monash.edu.au', 'pl1.eng.monash.edu.au', 'planetlab5.eecs.umich.edu', 'planetlab4.cs.uoregon.edu',
             'planetlab03.cs.washington.edu', 'pl1.rcc.uottawa.ca', 'planetlab01.cs.washington.edu',
             'planetlab-04.cs.princeton.edu', 'whitefall.planetlab.cs.umd.edu', 'node1.planetlab.albany.edu',
             'planetlab2.c3sl.ufpr.br', 'planetlab4.postel.org', 'planetlab-2.calpoly-netlab.net',
             'planetlab3.comp.nus.edu.sg', 'planetlab3.wail.wisc.edu', 'planetlab2.utdallas.edu',
             'node2.planetlab.mathcs.emory.edu', 'planetlab5.williams.edu', 'planetlab4.williams.edu',
             'node1.planetlab.mathcs.emory.edu', 'cs-planetlab3.cs.surrey.sfu.ca', 'planetlab2.dtc.umn.edu',
             'planetlab1.cs.uoregon.edu', 'planetlabone.ccs.neu.edu', 'planetlab1.comp.nus.edu.sg',
             'planetlab3.williams.edu', 'planetlab4.mini.pw.edu.pl', 'planetlab2.inf.ethz.ch',
             'planetlab5.ie.cuhk.edu.hk', 'planetlab2.cesnet.cz', 'planetlab1.cesnet.cz',
             'planetlab04.cs.washington.edu', 'planetlab02.cs.washington.edu', 'planetlab2.pop-mg.rnp.br',
             'planetlab1.pop-mg.rnp.br', 'planetlab2.cs.purdue.edu', 'planetlab2.koganei.itrc.net',
             'planetlab1.koganei.itrc.net', 'plink.cs.uwaterloo.ca', 'lefthand.eecs.harvard.edu',
             'planetlab1.dtc.umn.edu', 'planetlab-5.eecs.cwru.edu', 'planetlab1.postel.org', 'planetlab1.cs.ubc.ca',
             'ple2.cesnet.cz', 'nuc1.planet-lab.eu', 'planetlab-1.ing.unimo.it', 'iraplab1.iralab.uni-karlsruhe.de',
             'iraplab2.iralab.uni-karlsruhe.de', 'dschinni.planetlab.extranet.uni-passau.de', 'ple2.planet-lab.eu']


@parallel(pool_size=6)
def host_type():
    run('uname -a')


@parallel(pool_size=6)
def local_dns_latency():
    sudo("ping -c 10 `sudo cat /etc/resolv.conf|grep nameserver|head -n1|egrep -o '[0-9.]+'`| tail -1| awk '{print $4}' | cut -d '/' -f 2")


@parallel(pool_size=6)
def install_quic_dependencies():
    sudo('yum install -y libnet-devel')


@parallel(pool_size=6)
def disk_size():
    run('df -h')


@parallel(pool_size=6)
def simple_client():
    run('./server/simple_client gcp.xuebing.name')


@parallel(pool_size=6)
def simple_client_repeat():
    run('./server/simple_client gcp.xuebing.name')
    run('./server/simple_client gcp.xuebing.name')
    run('./server/simple_client gcp.xuebing.name')


@parallel(pool_size=6)
def init():
    sudo('yum install -y gcc-c++ bind-utils')


@parallel(pool_size=6)
def test_dns_delay():
    sudo('dig miss.xuebing.name|grep Query')
