"""
var1="Hello world"
var2=4
var3=36.7;
var4="44";77

var5=44;
# print(var1,var2,var3)
# print(type(var1))
# print(type(var2))
# print(type(var3))
# String and integer can't be added
#ex:-
#print(var1+var2) error
# print("\n",10*str(int(var4)+var5))
# print(10*"I am number 1\n")
print("Enter your number")
innum=input()#it take string
# intt=input()
print ("ypu entered ",int(innum)+44)
#quiz:1
#Only addition calculator
print("Enter number 1")
i=float(input())
print("Enter number 2")
j=int(input())
print("Addition is",i+j)#floating data type and integer data type can be added easily in python and result will be floating data type...
"""

#
var11="hello world"
var4="harry"
var1="1"
var2=4
var111=2
var3=33.33
print(type(var1))
print(type(var2))
print(int(var2)+var3)
print(int(var2)+int(var3))
print(float(var2)+float(var111))
print(str(var3)+var11)
# print(var11+var1)
# print (var1+var4)
# print(var2+var3)
# # print(var1+var2)
# print(type(var1))
# print(type(var2))
# print(type(var3))
# k=type(var2)
# print(k)
# k2=var2+var3
# print(type(k2))
# k3=var1+var4
# print(type(k3))
# var1=int (var1)
# print(100*(str((var1+var2)),"\n"))
"""Typecasting
function 
str()
int()
float()
"""
# print (10*"hello world returns \n")
# print (10*"hello world returns\n"*10)
# print("Enter your number")
# inpnum=input("enter number1")
# print("enter number 2")
# inpnum1=input("")
# print(inpnum+inpnum1)

# inpnum=int(input("enter number1"))
# print("enter number 2")
# inpnum1=int(input(""))
# print(inpnum+inpnum1)

# Quick quiz: make a calculator which add 2 numbers..
print("This calculator is only used to add 2 number:")
while(1):
    a = int(input("Enter number 1:"))
    b = int(input("Enter number 2:"))
    print("sum is",a+b)
    c=input("enter if you to exit then enter 1")
    if c=="1": break