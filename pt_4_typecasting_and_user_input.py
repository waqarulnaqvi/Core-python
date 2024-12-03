'''
Types of typecasting
1)Implicit typecasting :python kar rha hai..
2)Explicit typecasting :programmer kar raha hai..
'''

# 1)Implicit Typecasting:
c=1.9
print(type(c))
d=8
print(type(d))
e=c+d
print(type(e))#result will be in float (Implicit Typecasting)..

# 2)Explicit typecasting :
a=int(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
# c=int "45"  #Error
d=int ("3")
c='3'#String can be write as both ' ' single quote and " " double quote
print(a+b+int(c)+d)