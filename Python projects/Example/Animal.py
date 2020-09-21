class Animal(object):
    def __init__(self, animalName):
        print(animalName,'bark')

class Dog(Animal):
       def __init__(self):
           print('dog is loyal')
           super().__init__('Dog')

d1 = Dog()
