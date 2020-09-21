class example:
    weekend = True
    def isholiday(example):
        if example.weekend:
            print ("Today is a holiday!!")
        else:
            print ("Not holiday")
    def change(example):
       if example.weekend:
           example.weekend = False
       else:
           example.weekend = True

a = example()
a.isholiday()

b = example()
b.change()
b.isholiday()
