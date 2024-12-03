# list
x=[1,2,3]
# print(dir(x))
print(x.__add__)
# print(x.__ad__)#AttributeError: 'list' object has no attribute '__ad__'. Did you mean: '__add__'?

#tuple
x=(1,2,3)
print(dir(x))
print(x.__dir__())
# print(x.__add__)


class Person:
    """uhiuhiuiuui"""
    def __init__(self,age,name):
        self.name=name
        self.age=age

p=Person("john",30)
# print(p.__dict__)
print(dir(p))
print(p.__dir__())
# print(p.__doc__)

print(help(str))
# print(help(p))
# print(help(Person))