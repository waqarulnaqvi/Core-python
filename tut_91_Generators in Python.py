"""GENERATORS IN PYTHON:
A Generator function returns a generator object which can be used to generate the values one-by-one as you iterate over it.Generator are a powerful
tool for working with large or complex data sets,as they allow you to generate the values on-the-fly."""
def mygenerator():
    for i in range(5):
        yield i
#         Whenever you see a yield statement in a python program then we are always talking about the generator.

def book():
    for i in range(5):
        yield i
    # i=0
    # while i>=20000:
    #     yield i
    #     i = i + 1





gen=mygenerator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

bk=book()
print(next(bk))
print(next(bk))
print(next(bk))
print(next(bk))

for j in gen:
    print(j)