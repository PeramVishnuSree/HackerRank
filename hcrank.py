ncustomers = int(input())
customers = list()
for i in range(ncustomers):
    customers.append(input())

def log(lst):
    log = dict()
    for i in lst:
        if i not in log:
            log[i] = 1
        else:
            log[i] = log[i] + 1

    return log

def problem(dictionary,n) :
    lst1 = list()
    for key in dictionary:
        if (int(dictionary[key])/n)*100 >= 5:
            lst1.append(key)
    lst1.sort()
    return lst1

log = log(customers)
sol = problem(log,ncustomers)

for i in sol:
    print(i)
