class MyClass:
    """
    This is my 
    second class
    """
    
    a = 10
     
    
    def func(self):
        return f'Hello {self}'

        
    # def func2(cls):
    #     print(f"h {cls}")
 
# create a new MyClass
# firstobject = MyClass()
# secondobject = MyClass()

# print(firstobject.func())
# print(secondobject.func())


# # Output: <function MyClass.func at 0x000000000335B0D0>
# print(MyClass.func())
# print(MyClass.func(firstobject))





# print(MyClass.func(firstobject))


# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
# print(firstobject.func)
 
# # # Calling function func()
# # # Output: Hello
# firstobject.func()