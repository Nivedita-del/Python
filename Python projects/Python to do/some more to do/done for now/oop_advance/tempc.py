from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fromBirthYear( name, birthYear):
        age1 = str(date.today().year - birthYear)
        print(name + "'s age is: " + age1)

    def age(name,age):
        age = str(age)
        print(name + "'s age is: " + age)


person = Person.age('Adam', 19)
print(person)

person1 = Person.fromBirthYear('John',  1985)
print(person1)