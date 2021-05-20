n = int(input())
numbers = [int(x) for x in input().split(' ')]

log = dict()
for i in numbers:
    if i in log:
        log[i] = log[i] + 1
        continue

    log[i] = 1

m = 0
for key in log:
    if log[key] > m:
        m = log[key]

deletions = n - m
print(deletions)
