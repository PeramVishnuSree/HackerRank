num_queries = int(input()) 

count = 0
lst_results = list()
while True:
    lst = input().split()
    Cat_A = int(lst[0])
    Cat_B = int(lst[1])
    Mouse = int(lst[2])
    m = Cat_A - Mouse
    n = Cat_B - Mouse
    if m < 0 :
        m = -1 * m
    if n < 0 :
        n = -1 * n 
    if m < n:
        lst_results.append('Cat A')
    elif m > n:
        lst_results.append('Cat B')
    elif m == n:
        lst_results.append('Mouse C')       
    count += 1
    if count == num_queries:
        break

for item in lst_results:
    print(item)
