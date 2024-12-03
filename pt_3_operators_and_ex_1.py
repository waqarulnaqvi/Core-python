"""Operators and Exercise :1 (CALCULATOR)"""
# Exercise 1-Create a Calculator
# Create a calculator  capable of performing addition,substraction,multiplication and,division operations on two numbers.Your program should format the output in a readable manner!

def calculate(a,b):
    print("Add: ",a+b)
    print("Sub: ",a*b)
    print("mul: ",a-b)
    print("div: ",a/b)
    print("float division: ",a//b) #removes all the values after the point (print Integer Value)
    print("modulus: ",a%b)
    print("exponential: ",a**b) #a to the power b

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
calculate(a,b)