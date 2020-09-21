print(range(100))

my_list = list(range(10))
print(my_list)

even = list(range(0,10,2))
odd = list(range(1,10,2))
print(even)
print(odd)

my_string = "awsdfghjyhgfdesfdg"
print(my_string.index('e'))

decimals = range(0,100)
print(decimals)
my_range = decimals[3:40:3]
print(my_range)
print(my_range == range(3,40,3))
print(range(0,5,2)==range(0,6,2))
print(list(range(0,5,2)))
print(list(range(0,6,2)))

r = range(0,100)
print(r)

for i in r[::-2]:
    print(i)

print('='*50)
for i in range(99,0,-2):
    print(i)

print('='*50)
print(range(0,100)[::-2]== range(99,0,-2))

for i in range(0,100,-2):
    print(i)

