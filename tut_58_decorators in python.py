"""Python Decorators:
A decorator is a function that takes another function as an argument and return a new function that modifies the behavior of the original function .The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

@decorator_function
def my_function():
    pass
"""

def greet(func):
    # *args takes all the objects as tuples and **kwargs takes all the objects as dictionary.
    def mfunc(*args,**kwargs):
    # def mfunc(*args):#run
    # def mfunc(**kwargs):#Error
        print("Good Morning")
        func(*args,**kwargs)
        # func(*args)#run
        # func(**kwargs)#Error
        print("Thanks for using this function.")
    return mfunc
# @greet
def add(a,b,c):
    print(a+b+c)
@greet
def hello():
    print("Hello World")


hello()
# greet(hello())
# print()
# greet(hello)()
# greet(add)(1,2,3)
# print()
# greet(add)(1,2,3)
# greet(add(1,2,3))

import logging
# def log_function_call(func):
#     def decorated(*args,**kwargs):
#         logging.info(f"Calling {func.__name__} with args={args},kwargs={kwargs}")
#         result=func(*args,**kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
#
# @log_function_call
# def my_function(a,b,c):
#      return a+b
# print(my_function(1,3,"erer"))
# print(log_function_call(my_function)(1,9,"erer"))