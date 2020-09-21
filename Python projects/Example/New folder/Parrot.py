class MyClass:
    __hiddenVariable = 10
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
    def __str__(self):
        return "From str method of Test: a is %s," \
               "b is %s" % (self.a, self.b)
