string = input()
length = len(string)
n = int(input())
count = 0

if n%length == 0:
    x = int(n/length)
    for i in string:
        if i == "a":
            count +=1
    count = count*x

elif n%length != 0:
    x = int((n//length))
    for i in string:
        if i == "a":
            count +=1
    string1 = string[:n%length]
    m = 0
    for i in string1:
        if i =="a":
            m +=1
    count = (count*x)+m

print(count)
