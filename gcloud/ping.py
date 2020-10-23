import paramiko
import re
from google.auth import compute_engine

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
key = paramiko.RSAKey.from_private_key_file('/home/aerberzhou/google_compute_engine')
for i in range(0,len(list)):
    ssh = paramiko.SSHClient()
    know_host = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(know_host)

    ssh.connect(
        hostname = list[i],
        username = 'ws',
        pkey=key
    )
    
    ssh_shell = ssh.invoke_shell()   
         
    for j in range(0,len(list)):
        print('instance-'+str(i+1)+' -> instance-'+str(j+1)+'\n')
        f.write('instance-'+str(i+1)+' -> instance-'+str(j+1)+'\n');
        command = 'ping -c 15 ' + list[j] + '\n'
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode()
        f.write(result)
        f.write('\n')
        
    ssh.close()

f.close()

