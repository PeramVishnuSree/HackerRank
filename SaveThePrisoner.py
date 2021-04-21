def func(prisoners,treats,start):
    x = (start + treats)-1
    x = x - (prisoners*(x//prisoners))
    if x == 0:
        x = prisoners
    return x

n = int(input())
for i in range(n):
    lst = input().split(' ')
    a = int(lst[0])
    b = int(lst[1])
    c = int(lst[2])

    print(func(a,b,c))
