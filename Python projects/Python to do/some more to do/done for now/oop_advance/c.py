from datetime import date

# random Person
class Person:
    def __init__(self,age):
        self.name = name
        self.age = age

    @staticmethod
    def fromBirthYear( birthYear):
        return date.today().year - birthYear

    def display(self):
        print( "'s age is: " + str(self.age))

person = Person( 19)
person.display()

person1 = Person.fromBirthYear(1985)
person1.display()