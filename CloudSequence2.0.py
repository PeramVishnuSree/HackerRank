n,k = [int(x) for x in input().split(' ')]
cloudlst = input().split()
e = 100

cycles = int(n%k)
cloudstr = ''
for i in cloudlst:
    cloudstr = cloudstr+i
if cycles != 0:
    cloudstr = cloudstr*k
    n = n*k
    
m = k
while m <n:
    i = cloudstr[m]
    if i == '0':
        e = e-1
    elif i == '1':
        e = e-3
    m = m+k

if cloudstr[0] == '0':
    e = e-1
else:
    e = e-3
print(e)
