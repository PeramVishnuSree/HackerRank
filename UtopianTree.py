def double(a):
    x = 2*a
    return x

def increasebyone(a):
    x = a+1
    return x

inputs = int(input())
while inputs > 0:
    height = 1
    inputs = inputs - 1
    cycles = int(input())
    while cycles >0:
        height = double(height)
        cycles = cycles - 1
        if cycles > 0:
            height = increasebyone(height)
            cycles = cycles - 1

    print(height)
