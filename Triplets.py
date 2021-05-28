n,d = [int(x) for x in input().split(' ')]
array = [int(x) for x in input().split(' ')]
sol = 0

for p_index in range(n):
    que = "No"

    for s_index in range(n):
        if p_index == s_index: continue
        if array[s_index] - array[p_index] == d:
            que = "Yes"
            continue

        if que == "Yes" and array[s_index] - array[p_index] == 2*d:
            sol +=1
            break

print(sol))
