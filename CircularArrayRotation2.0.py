n,k,q = [int(x) for x in input().split(' ')]
ar = [int(x) for x in input().split(' ')]

#Instead of altering the actual array, we find the solution by
#mathematical manipulation for better efficiency.
if k%n == 0:
    pass
else:
    k = k - (n*(k//n))

for i in range(q):
    index = int(input())
    if index <= (n-k):
        sol = ar[index+(n-k)]
    elif index > (n-k):
        sol = ar[index-k]
    print(sol)
