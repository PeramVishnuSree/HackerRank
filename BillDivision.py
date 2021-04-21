paras = input().split(' ')
ind_item = int(paras[1])
num_items = int(paras[0])
bill = [int(x) for x in input().split(' ')]
amount = int(input())
actual_amount = (sum(bill)-bill[ind_item])/2

if amount == actual_amount:
    print('Bon Appetit')
else:
    nd = (str(amount-actual_amount)).split('.')
    print(nd[0])
