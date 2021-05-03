testcases = int(input())

def f(num1,num2) :
    import math
    count = int(math.sqrt(num2)) - int(math.sqrt(num1))
    if int(math.sqrt(num1)) - math.sqrt(num1) == 0:
        count = int(math.sqrt(num2)) - int(math.sqrt(num1)) + 1
    print(count)

for i in range(testcases):
    a,b = [int(x) for x in input().split(' ')]
    f(a,b)
