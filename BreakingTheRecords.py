num_entries = int(input())

min_count = 0
max_count = 0
smallest = None
largest = None

scores = input().split()

for i in scores:
    if smallest is None:
        smallest = int(i)
    elif int(i) < smallest:
        min_count += 1
        smallest = int(i)
       
    if largest is None:
        largest = int(i)
    elif int(i) > largest :
        max_count += 1
        largest = int(i)
        
print(max_count,min_count)
