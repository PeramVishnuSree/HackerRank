def function(lst,cycles):
    l = len(lst)
    for i in range(cycles):
        lst = [lst.pop()]+lst[:l]
    return lst

paras = input().split(' ')
cycles = int(paras[1])
queries = int(paras[2])

lst = input().split(' ')
finallst = function(lst,cycles)

while True:
    try:
        x = int(input())
        print(finallst[x])
    except EOFError:
        break
