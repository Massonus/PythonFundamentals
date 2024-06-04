class Animal():
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        return "Sound"


class Mammal(Animal):

    def make_sound(self):
        return "Roar"


class Bird(Animal):

    def make_sound(self):
        return "Squawk"


class Reptile(Animal):
    def make_sound(self):
        return "Hiss"


animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]

for animal in animals:
    print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")
