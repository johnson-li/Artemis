import re
f = open("output.txt", "r")

x = 0
y = 0
dis = [[0 for i in range(13)] for j in range(13)]
a = [0 for i in range(7)]
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
        dis[x][y] = a[3]
        #dis[x][y] = (a[1]+a[2]+a[3]+a[4]+a[5])/5
            
for i in range(1,11):
    for j in range(1,11):
        print('%.2f'%dis[i][j],end=' ')
    print()
print()

for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if (dis[i][j]+dis[j][k]<dis[i][k]):
                tmp = dis[i][j]+dis[j][k]
                print(i,j,k)
                print('%.2f'%tmp,'%.2f'%dis[i][k])
                print()
            
f.close()

