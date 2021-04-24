n = int(input())

def function(num):
    count = 0
    #num should be in string format
    length = len(num)
    for i in range(length):
        x = num[i-1]
        if int(x) != 0 and int(num)%int(x) == 0:
            count +=1

    return count

for i in range(n):
    num = input()
    sol = function(num)
    print(sol)
