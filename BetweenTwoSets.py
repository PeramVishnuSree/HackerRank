para = input().split(' ')
number_factors = int(para[0])
number_multiples = int(para[1])

factors = input().split(' ')
multiples = input().split(' ')

factors_list = list()
for i in factors:
    i = int(i)
    factors_list.append(i)

multiples_list = list()
for i in multiples:
    i = int(i)
    multiples_list.append(i)

limit = min(multiples_list)
final_list = list()

for i in range(1,limit+1):
    count = 0
    for x in factors_list:
        if i%x == 0:
            count +=1
            if count == number_factors:
                final_list.append(i)

n=0
for i in final_list:
    count = 0
    for x in multiples_list:
        if x%i == 0:
            count +=1
            if count == number_multiples:
                n +=1

print(n)
