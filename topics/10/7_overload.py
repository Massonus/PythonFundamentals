# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"Information From repr_({self.x},{self.y})"
    
#     def __str__(self):
#         return f"That is Point ({self.x},{self.y})"


# print(dir(Point))

# p1 = Point(2,3)
# # print(type(p1))
# # print(p1)
# p2 = Point(-1,2)

# print(p1)
# print(p2)

# print(p1 + p2)

# ##############################
# #special function

# # p1 = Point(2,3)
# # print(p1)
# # # <__main__.Point object at 0x00000000031F8CC0>
# # print(str(p1))
# # # '(2,3)'

# # print(format(p1))

# #########################################
# # Special Functions in Python
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)

# p1 = Point(2,3)
# print(p1)
# # (2,3)

# # print(str(p1))
# # # '(2,3)'

# # print(format(p1))
# # '(2,3)'
# ########################################
# #Overloading Operators
# add
###########################

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "That is point ({0},{1})".format(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x 
        y = self.y + other.y
        return Point(x, y)

p1 = Point(2,3)
p2 = Point(-1,2)
# print(p1)
# print(p2)
# # # # # # # # # # # # # # # # #
p3 = p1 + p2
print(p3)


# # (1,5)

# ################################
# # #overload comparison operators
# ################################
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
    
#     def __lt__(self, other):
#         self_mag = self.x ** 2 + self.y ** 2
#         other_mag = other.x ** 2 + other.y ** 2
#         return self_mag < other_mag

# print(Point(1,1) < Point(-2,-3))

# # # # # # # # # # # # # True
 
# print(Point(1,1) < Point(0.5,-0.2))
# # # False
 
# # # # print(Point(1,1) < Point(1,1))
# # # # False



