
class MyClass: 
    
    def __init__(self, age = 0): 
        self._age = age
        print("Call __init__")  
     # function to get value of _age
    
    def get_age(self):
        print("Call from getter --> get_age")
       #  print("getter method called") 
        return self._age
    # function to set value of _age 
    
    def set_age(self, a): 
        print("setter method called") 
        #  print("self.set_age")
        if a < 18: 
            print("Sorry you age is below eligibility criteria") 
        else: 
            self._age = a
    # function to delete _age attribute 
    
    def del_age(self): 
       print("self----del_age")
       del self._age 
     
    age = property(get_age, set_age, del_age)  

mark = MyClass(45) 
print(mark.age)

mark.age = 111
print(mark.age)

