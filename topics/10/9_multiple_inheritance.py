class Polygon:
    
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) 
                                              for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")
 
            
class Triangle(Polygon):
    """
    docstring
    """
    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(3)
                
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        p = (a + b + c) / 2
        area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print(f"The area of the triangle is {area}")  

class Rectangle(Polygon):
    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(2)
                
    def findAreaRect(self):
        a, b = self.sides
        # calculate the semi-perimeter
        area = a*b
        print(f"The area of the rectangle is {area}")    

#########4

t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

# w = Rectangle()
# w.inputSides()
# w.dispSides()
# w.findAreaRect()
# print(Triangle.__mro__)
# print(Triangle.__dict__)
# print(Polygon.__dict__)
# # t.inputSides()
# t.dispSides()
# t.findArea()

# The area of the triangle is 6.00
#########################

# print(isinstance(t, Triangle))
# # # True
# print(isinstance(t, Polygon))
# # # True
# print(isinstance(t, int))
# # # False
# print(isinstance(t, object))
# # # # True

# # # #########################
# print(issubclass(Polygon, Triangle))
# # # # False

print(Triangle.__mro__)

# print(issubclass(Triangle, Polygon))
# # True
# print(issubclass(bool, int))
# # # True
# # ##########################
# # # class Base:
# # #     pass
  
# # class Derived1(Base):
# #     pass
  
# # class Derived2(Derived1):
# #     pass
# # ##################
# # # Output: True
# # print(issubclass(list, object))
 
# # # Output: True
# # print(isinstance(5.5, object))
 
# # # Output: True
# # print(isinstance("Hello", object))
# # ##########################

# # print(Derived2.__mro__)

 
# ########################
# class X: 
#     pass
# class Y: 
#     pass
# class Z: 
#     pass
 
# class A(X,Y): 
#     pass
# class B(Y,Z): 
#     pass
 
# class M(B,A,Z): 
#     pass
 
# # # # # Output:
# # # # # [<class '__main__.M'>, <class '__main__.B'>,
# # # # # <class '__main__.A'>, <class '__main__.X'>,
# # # # # <class '__main__.Y'>, <class '__main__.Z'>,
# # # # # <class 'object'>]
# print(M.mro())
# print(M.__mro__)

