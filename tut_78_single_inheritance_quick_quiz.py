# 12 7
"""
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def make_sound(self):
        print("Bark!")

a=Animal("Russo","Dog")
a.make_sound()

d=Dog("Russo","German Shifered")
d.make_sound()
"""
# Quick Quiz: Implement a Cat class by using the animal class.Add some methods specific to cat
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("Sound made by the animal")

class Cat(Animal):
    def __init__(self,name,breed):
        # Animal.__init__(name,"Cat")
        self.breed=breed
        super().__init__(name,"CAt")
    def make_sound(self):
        print("Miyao Miyao")

a=Animal("Tom","Cat")
a.make_sound()
print(a.name)
print(a.species)
print()

c=Cat("Tommy","Persian")
c.make_sound()
print(c.breed)
print(c.name)
print(c.species)