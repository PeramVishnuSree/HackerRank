num_steps = int(input())
paras = input()
count = 0
num_valleys =  0
parameters = list()
parameters.append(paras[0])
for i in range(1,len(paras)):
    parameters.append(paras[i])

for i in parameters:
    if count == 0 :
        if i == "U" :
            count += 1
        elif i == "D" :
            count -= 1
            num_valleys += 1
    else:
        if i == "U" :
            count += 1
        elif i == "D" :
            count -= 1
            
print(num_valleys)
