#Create dynamic list of lists
import ctypes

class MyList:
    def __init__(self):
        self.size = 1 
        self.n = 0
        #create a C type array with size = self.size
        self.A = self.__make_array(self.size)
    
    
    def __len__(self):
        return self.n
    
    
    def append(self, item):
        if self.n == self.size:
            self.__resize(2 * self.size)
            self.A = self.__make_array(2 * self.size)   
            
    def __make_array(self,capacity):
        return (capacity * ctypes.py_object)()

L = MyList()

print (L, len(L))  # prints: MyList() 0