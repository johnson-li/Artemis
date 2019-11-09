import paramiko
import re
from google.auth import compute_engine
import threading 

def ssh_machine(i,ip,user,key,command):
    ssh = paramiko.SSHClient()
    know_host = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(know_host)
    ssh.connect(
        hostname = ip,
        username = user,
        pkey = key
    )
    ssh_shell = ssh.invoke_shell() 
    
    for j in range(len(command)):
        print('instance-'+str(i+1)+' -> instance-'+str(j+1)+'\n')
        stdin, stdout, stderr = ssh.exec_command(command[j])
        result = stdout.read().decode()
        threadLock.acquire()
        f.write('instance-'+str(i+1)+' -> instance-'+str(j+1)+'\n');
        f.write(result)
        f.write('\n')
        threadLock.release()
        
    ssh.close()

if __name__ == '__main__':

    f = open("list.txt", "r")

    a = []
    num = []
    list = []
    while True:
        x = f.readline()
        if not x:
            break
        y = x.split()
        if y[0][0]=='i':
            number = re.findall(r"\d+\.?\d*",y[0])
            num.append(int(number[0])-1)
            a.append(y[4])
    for i in range(len(a)):
        for j in range(len(a)):
            if num[j]==i:
                list.append(a[j])
    f.close()
    print(list)
    f = open("output.txt", "w") 
    f.truncate()

    #key = paramiko.RSAKey.from_private_key_file('C:/Users/ws/.ssh/google_compute_engine')
    key = paramiko.RSAKey.from_private_key_file('/home/wch19990119/google_compute_engine')
    
    command = []
    for i in range(20):
        command.append('ping -c 15 ' + list[i] + '\n')
    username = 'ws'
    threads = []
    threadLock = threading.Lock()
    for i in range(20):
        a = threading.Thread(target=ssh_machine,args=(i,list[i],username,key,command))   
        threads.append(a)
        a.start()
 
    for t in threads:
        t.join()

    f.close()

