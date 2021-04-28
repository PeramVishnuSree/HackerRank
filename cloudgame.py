n = int(input())
clouds = [int(x) for x in input().split(' ')]

i = 0
count = 0

while i < n-1:
    if i+2 <= n-1 and clouds[i+2] == 0:
        i = i+2
        count +=1

    else:
        i = i+1
        count +=1

print(count) 
