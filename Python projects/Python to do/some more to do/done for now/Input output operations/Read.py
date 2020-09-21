o = open("daffodils.txt",'r')
for line in o:
    if "and" in line.lower():
        print(line, end='')

o.close()
print('\n')
print('-'*40)
with open("daffodils.txt",'r')as o:
    for line in o:
        if "AND" in line.upper():
            print(line, end='')
print('\n')
print('-'*40)
with open('daffodils.txt','r') as o:
    lines = o.readlines()
print(lines)




