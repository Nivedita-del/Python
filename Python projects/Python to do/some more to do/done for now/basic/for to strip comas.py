number = "9,2,342,445,654,234,3425"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i],end='')

