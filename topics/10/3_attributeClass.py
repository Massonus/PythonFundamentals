class Parrot():
 
    # class attribute
    species = "bird"
 
    # instance attribute
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind

    def say_hello(self):
        return f"{self.name} say hello!!! "


    
# instantiate the Parrot class
parr1 = Parrot("Blue", 5, "ARO1")
parr2 = Parrot("Woo", 15, "ARO2")

print(Parrot.species)
print(parr1.species)



# # access the class attributes
print("Blu is a {}".format(parr1.species))
print("Woo is also a {}".format(parr2.__class__.species))

 
# # # access the instance attributes
print("{} is {} years old".format( parr1.name, parr1.age))
print("{} is {} years old".format( parr2.name, parr2.age))

# print(parr1.say_hello())
# print(parr2.say_hello())

