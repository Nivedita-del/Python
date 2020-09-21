class Kasturba:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def max(x,y):
        a = x
        b = y
        if (a>b):
            print(a)
        else:
            print(b)

    def stringCopy(string, index):
        index = int(index)
        z = len(string)
        actualIndex = int(z - index)
        for i in range(actualIndex):
            first = ''
            first = first+ string[i]
        i = int(actualIndex)
        for i in range(z):
            last = ''
            last += string[i]
        print (first+last)

    def pwr(x,y):
        c = int(x)
        d = int(y)
        i = 1
        if (d == 0):
            return 1
        else:
            ans = 1
            for i in range (d):
                ans *=c
            print(ans)

inx = input("Enter the x elements ")
iny = input("Enter the y elements ")
out = Kasturba(inx,iny)
out = Kasturba.pwr(inx,iny)
outmax = Kasturba.max(inx, iny)
outstr = Kasturba.stringCopy("hello", 1)
print(out)

an this