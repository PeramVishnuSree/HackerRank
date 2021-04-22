nele = int(input())
lst = [int(x) for x in input().split(' ')]

for i in range(1,nele+1):
    x = lst.index(i) + 1
    x = lst.index(x) + 1
    print(x)
