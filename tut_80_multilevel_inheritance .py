# Multi-level Inheritance:
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

class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,"German sheefward")
        # super().__init__(name,"Germanshefward")
        self.color=color

    def show_details(self):
        Dog.make_sound(self)
        print(f"Color : {self.color}")

a=Animal("Russo","Dog")
a.make_sound()
print(Animal.mro())
print()

d=Dog("Russo","German Shifered")
d.make_sound()
print(Dog.mro())
print()

o=GoldenRetriever("toto","Black")
o.show_details()
print(GoldenRetriever.mro())
print()