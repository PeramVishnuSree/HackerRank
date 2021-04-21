days = int(input())

shared = 5
lst = list()
for i in range(days):
    liked = shared//2
    lst.append(liked)
    shared = liked*3

sol = sum(lst)
print(sol)
