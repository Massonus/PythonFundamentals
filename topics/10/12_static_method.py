class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'

obj_1 = MyClass()
obj_2 = MyClass()

# print(MyClass.method())
# print(obj_1.method())
# print(obj_2.method())

# print(MyClass.classmethod())
# print(obj_1.classmethod())

# print(MyClass.staticmethod())
# print(obj_1.staticmethod())
# print(obj_2.staticmethod())









###########################
# print(obj_1.method())
# print(MyClass.method(obj_1))
# print(MyClass.method(obj_1))
###########################
# print(obj_1.classmethod())
# print(MyClass.classmethod())
# # # # ###########################
# print(obj_1.staticmethod())
# print(MyClass.staticmethod())



