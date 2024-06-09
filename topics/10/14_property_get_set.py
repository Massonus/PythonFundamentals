class MyClass: 
     def __init__(self): 
        self._age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
        print("getter method called") 
        return self._age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria") 
        print("setter method called") 
        self._age = a

     @age.deleter
     def age(self):
        self._age = 'No more' 
  
   
mark = MyClass() 
  
mark.age = 33
  
print(mark.age) 