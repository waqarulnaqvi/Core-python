class Person:
    name="Harry"
    occupation="Software Developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
a.info()
# print(a.name)
# print(a.occupation)
a.name="Shubham"
a.occupation="Accountant"
# print(a.name,a.occupation)
a.info()
print()
b=Person()
b.name="Nitika"
b.info()
a.info()
# Self parameter:
"""The self parameter is a reference to the current instance of the class,  and is used to access variable that belongs to the class.

It must be provided as the extra parameter inside the method definition.
'In simple words self meaning those object in which this method is calling.'
'Example:
c=Person()
c.info() #here c is a object in which self is calling so c=self
"""
