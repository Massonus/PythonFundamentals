class Parrot:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
 
    def dance(self):
        return f"{self.name} is now dancing"
 

# instantiate the object
blue_2 = Parrot("Blue", 10)

green_1 = Parrot("Green", 25)
 
# call our instance methods
print(blue_2.sing("\"Happy\""))
print(blue_2.dance())

print(green_1.sing("\"Sad\""))
print(green_1.dance())




