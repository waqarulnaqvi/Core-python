"""__init__ it is also called as dunder method."""
class Person:
    # def __init__(self,n="Azaan",occ):#SyntaxError: non-default argument follows default argument
    def __init__(self,n,occ="Codder"):#Constructor
        self.name=n#In python Constructor always return none.
        self.occ=occ
        print("Hey I am a person")

    def info(self):
        print(f"{self.name} is a {self.occ}")

    name = "Harry"
    occ = "Developer"
# self passes automatically in a class or a respective object passes automatically in a class. In the below example "a" is that object.
a=Person("Yum","meow")
a.info()
b=Person("Azaan")
b.info()