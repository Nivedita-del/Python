class example:
    weekend = True
    def isholiday(self):
        if self.weekend:
            print ("Today is a holiday!!")
        else:
            print ("Not holiday")
    def change(self):
       if self.weekend:
           self.weekend = False
       else:
           self.weekend = True

a = example()
a.isholiday()

b = example()
b.change()
b.isholiday()
