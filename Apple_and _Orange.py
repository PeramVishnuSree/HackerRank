st = input().split()
house_cordl = st[0]
house_cordr = st[1]
 
ab = input().split()
apple_tree = ab[0]
orange_tree = ab[1]

mn = input().split()
num_apples = mn[0]
num_oranges = mn[1]

dist_apples = input().split()
dist_oranges = input().split()

for i in dist_apples:
    if int(i) < 0:
        dist_apples.remove(i)

for i in dist_oranges:
    if int(i) > 0:
        dist_oranges.remove(i)

def return_count(dist_fruits, dist_tree,a,b) :
    count = 0
    for i in dist_fruits:
        x = int(i) + int(dist_tree)
        if x<= int(a) and x >= int(b):
            count +=1
    return count

print(return_count(dist_apples, apple_tree, house_cordr, house_cordl))
print(return_count(dist_oranges, orange_tree, house_cordr, house_cordl))
