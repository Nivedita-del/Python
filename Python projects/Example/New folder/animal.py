from abc import ABCMeta, abstractmethod, abstractproperty
class AbstractAnimal(metaclass=ABCMeta):
    @abstractmethod
    def make_noise(self):
        pass
    
    @abstractmethod
    def species(self):
        pass
    def getname(self):
        pass
    def setname(self, value):
        pass
    
    name = abstractproperty(getname, setname)
    def is_alive(self):
        return True
    
class Dog(AbstractAnimal):
    pass
