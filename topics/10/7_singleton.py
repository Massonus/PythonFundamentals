class Singleton():
    # attribute for storing a single copy
    obj = None 
    
    def __new__(cls, *args, **kwargs): # class Singleton.
        if cls.obj is None:
            # If it does not yet exist, then
            # call __new__ of the parent class	
            cls.obj = object.__new__ (cls, *args, **kwargs)
        return cls.obj # will return Singleton

    

object_1 = Singleton()
print(object_1)

object_1.Attr = 12

print(object_1.Attr)      
# # # # ####
new_second_objectect = Singleton()
print(new_second_objectect)
print(new_second_objectect.Attr)                       
# # # ###
# # print(new_objectect is object_1)
# #  # new_object and object_1 is one and the same object
# # #  True



