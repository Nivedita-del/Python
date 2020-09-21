import math
class triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("",area)
    def perimeter(self):
        if (((a + b) > c) & ((b + c) > a) & ((c + a) >b)) :
            print ("Valid")
        else:
            print("not valid")
a=int(input("a =  "))
b = int(input("b = "))
c = int(input("c = "))
obj=triangle(a,b,c)
obj.area()
obj.perimeter()
