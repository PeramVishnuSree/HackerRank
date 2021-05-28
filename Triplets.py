n,d = [int(x) for x in input().split(' ')]
array = [int(x) for x in input().split(' ')]
sol = 0

for p_index in range(n):
    for s_index in range(n):
        if p_index == s_index: continue
        if array[s_index] - array[p_index] == d:

            for i in range(s_index,n):
                if array[i] - array[s_index] == d:
                    sol +=1

print(sol)
