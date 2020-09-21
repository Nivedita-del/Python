class cal:
    def __init__(self,val1,val2):
        self.value1 = val1
        self.value2 = val2

    def add(self):
        addition = self.value1+self.value2
        print(addition)

    def sub(self):
        minus = self.value1-self.value2
        print(minus)

    def mul(self):
        multiply = self.value1*self.value2
        print(multiply)

    def div(self):
        divide = float(self.value1/self.value2)
        print(divide)
val1 = int(input('Enter first number'))
val2 = int(input('Enter second number'))
print('''Choose 
add
sub
mul
div''')
c = input('operation')

d = cal(val1,val2)
if(c == 'add'):
    d.add()
elif(c == 'sub'):
    d.sub()
elif(c == 'mul'):
    d.mul()
elif(c == 'div'):
    d.div()

