"""Built in function"""
a=9
b=8
#c=sum((a,b))
#print(sum((a,b)))
"""User define function"""
def func1():
    print("Hello i am a user define function 1")
#print(func1())
#func1()
def func2(a,b):
    """This is a function of Addition of a two number""" #Function first line multi line comment  is called doc string.
    print("Adition of a and  b is:",end="")
    return a+b
print(func2(5,8))
print(func2.__doc__)

