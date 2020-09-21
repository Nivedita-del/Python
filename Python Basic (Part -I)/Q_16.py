''' Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.'''
print("Enter a number")
a = int(input())
if (a>17):
    temp = a-17
    b = temp*2
    print(b)
elif(a<17):
    c = 17 - a
    print(c)
else:
    print('0')