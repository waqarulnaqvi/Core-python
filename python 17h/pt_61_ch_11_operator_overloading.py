"""jis method me __(double underscore) use hota usse hum dunder method kehte hai..
Ex: 1)__init__,2)__class__ etc
        1)init
        def __init__(self,name,salary,subunit) :
        we will use same name in both of the side in most the cases..
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

       2)__class__ 
       def changeSalary(self, sal):# it changes the class attribute..
           self.__class__.salary=sal #dunder class to change class    attributes method..
"""
# from audioop import mul

class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):#__add__ method given hai python official documentaion me agar aapko + overload karna to use karre..
        print("Lets add")
        return self.num +num2.num

    def __mul__(self,num2):#__mul__ method given hai python official documentaion me agar aapko * overload karna to use karre..
        print("Lets multiply")
        return self.num *num2.num

n1= Number(4)#n1 and n2 are not a integer..they are a Number object..            
n2= Number(6)#n1 and n2 are not a integer..they are a Number object..
sum=n1+n2
# sum=n1*n2
mul=n1*n2
print(sum)
print(mul)
"""Operator overloading in Python:
Operator in python can be overloaded using dunder methods.
These methods are called when a given operator is used on the object..

#Mostly yahi method use karoge agar app operator overloading karoge pyton me..
Operator in python can be overloaded using the following methods:
p1+p2  -> p1.__add__(p2)
p1-p2  -> p1.__sub__(p2)
p1*p2  -> p1.__mul__(p2)
p1/p2  -> p1.__truediv__(p2)
p1//p2  -> p1.__floordiv__(p2)

Other dunder/magic methods in python:
__str__() ->used to set what gets displayed upon calling str(obj)..
"""