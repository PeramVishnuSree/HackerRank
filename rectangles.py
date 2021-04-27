n = int(input())
k = input()
rectangles = list()
for i in range(n):
    x = [int(i) for i in input().split(' ')]
    rectangles.append(x)

count = 0
m = 0
for i in rectangles:
    for x in rectangles:
        if rectangles.index(i) != rectangles.index(x) and (i[0]/x[0]) == (i[1]/x[1]) :
            count +=1
print(int(count/2))
