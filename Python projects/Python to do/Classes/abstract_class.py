
from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractAnimal(metaclass=ABCMeta):

    # abstract method
    @abstractmethod
    def make_noise(self):
        pass

    # an abstract read-only-property
    @abstractproperty
    def species(self):
        pass
  
    # abstract read/write property
    def getname(self):
        pass
    
    def setname(self, value):
        pass

    name = abstractproperty(getname, setname)
    
    # non-abstract method
    def is_alive(self):
        return True



"""
Exercise: Implement the Dog class so that the code below runs.
"""
class Dog(AbstractAnimal):
    pass

rex = Dog()
print(Dog.is_alive())
rexmake_noise()
print(rex.species())

print(rex.name)
