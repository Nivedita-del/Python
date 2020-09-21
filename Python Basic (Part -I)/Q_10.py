''' Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615'''
n = int(input())
a = int("%s" % n)
b = int ("%s%s" % (n,n))
c = int("%s%s%s" % (n,n,n))
print(a+b+c)