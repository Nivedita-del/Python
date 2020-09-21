import random
dict = {'num' : ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'],
        'col' : ['red','black'],
        'symbol':["club","diamond","heart","spade"]}
numKey = dict['num']
colKey = dict['col']
symKey = dict['symbol']
n = int(input("how many number of cards u want? "))
print('Your card')
for i in range(n-1):
    n = random.randint(0, len(numKey) - 1)
    c = random.randint(0, len(colKey) - 1)
    s = random.randint(0, len(symKey) - 1)
    print(colKey[c],symKey[s],numKey[n])

