n = int(input())
array = [int(x) for x in input().split(' ')]

def function(sticks):
    while len(sticks) >=1:
        print(len(sticks))
        x = min(sticks)

        #removing the elements with the minimum value
        while x in sticks:
            sticks.remove(x)

        #reducing the value of every element by the minimum value
        for i in range(len(sticks)):
            sticks[i] = sticks[i] - x

function(array)
