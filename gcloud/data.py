import matplotlib.pyplot as plt
import re

sz = 21

#handle the data
f = open("result/output2.txt", "r")
x = 0
y = 0
dis = [[0 for i in range(23)] for j in range(23)]
diff = [[0 for i in range(23)] for j in range(23)]
a = [0 for i in range(16)]
while True:
    s = f.readline()
    if not s:
        break
    if s[0]=='i':
        number = re.findall(r"\d+\.?\d*",s)
        x = int(number[0])
        y = int(number[1])
    if s[0]=='6':
        number = re.findall(r"\d+\.?\d*",s)
        k = int(number[3])
        a[k] = float(number[5])
    if s[0]=='r':
        a.sort()
        #dis[x][y] = a[8]
        dis[x][y] = min(a[1:])
f.close()

#get the cities/countries
#f = open("address.txt", "r")
addr = [0 for i in range(sz)]
for i in range(1,sz):
    #s = f.readline()
    addr[i] = 'dc-%d' % i
f.close()

for i in range(1,sz):
    for j in range(1,sz):
        print('%.2f'%dis[i][j],end=' ')
    print()
print()

#get the diff matrix(one_jump-direct)
cnt = [0 for i in range(sz)]
dx = []
dy = []
p = []
for i in range(1,sz):
    for j in range(1,sz):
        if i==j:
            continue
        dmin = 1000000
        for k in range(1,sz):
            if i!=k and j!=k:
                if dis[i][k]+dis[k][j]-dis[i][j]<dmin:
                    dmin = dis[i][k]+dis[k][j]-dis[i][j]
                    tmp = k
        dx.append(dmin)
        diff[i][j] = dmin
        if dmin<0:
            #print(i,tmp,j)
            print(addr[i],'->',addr[tmp],'->',addr[j])
            print('%.2f'%(dis[i][tmp]+dis[tmp][j]),'%.2f'%dis[i][j])
            p.append([dmin,str(addr[i])+' -> '+str(addr[tmp])+' -> '+str(addr[j])])
            cnt[tmp] = cnt[tmp]+1
print()

'''
#print
for i in range(1,sz):
    for j in range(i+1,sz):
        if abs(dis[i][j]-dis[j][i])>=4:
            #print('%.2f'%(dis[i][j]-dis[j][i]),end=' ')
            print(addr[i],'|',addr[j],' ','%.2f'%dis[i][j],' ','%.2f'%dis[j][i])
print()
'''

#print
p.sort()
for i in range(len(p)):
    print('%.2f'%p[i][0],p[i][1])
print()


#print
tot = 0
for i in range(1,sz):
    print(addr[i],cnt[i])
    tot = tot+cnt[i]
print(tot)
print()

#show the CDF
dx.sort()
for i in range(len(dx)):
    dy.append((i+1)/len(dx))
plt.plot(dx,dy)
plt.show()
