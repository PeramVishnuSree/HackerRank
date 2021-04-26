testcases = int(input())

def function(a,b):
    count = 0
    for i in range(a,b+1):
        if i**(1/2) == int(i**(1/2)):
            count +=1
    return count

for i in range(testcases):
    a,b = [int(x) for x in input().split(' ')]
    print(function(a,b))
    
