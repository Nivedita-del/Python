class Temp:
    def __init__(self,temp = 0 ):
        self.set_temp(temp)
        
    def far(self):
        return(self._temp()*1.8)+32
    
    def get_temp(self):
        print("get value")
        return self._temp
    
    def set_temp(self,value):
        if value < -273:
            raise ValueError("Welcome to science 101")
        print("set value")
        self._temp = value
temp = property(get_temp, set_temp)
