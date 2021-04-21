n = int(input())
p = int(input())

# From front
if p%2 != 0:
    front = (p-1)/2
elif p%2 == 0:
    front = p/2

#From back
#if n is odd
if n%2 != 0:
    if p%2 != 0:
        back = (n-p)/2
    elif p%2 == 0:
        back = (n-p-1)/2
#if n is even
elif n%2 == 0:
    if p%2 == 0:
        back = (n-p)/2
    elif p%2 != 0:
        back = (n-p+1)/2

if front<back:
    ans = front
elif front>back:
    ans = back
else:  #if front and back are equal
    ans = back

ans = str(ans)
ans = ans.split('.')
print(ans[0])
