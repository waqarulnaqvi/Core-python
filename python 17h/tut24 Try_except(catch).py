# Mostly try and catch use in a internet connectivity loss to save user program.
a=input("Enter number 1: ")
b=input("Enter number 2: ")
try:
    print("sum is ",
          float(a)+float(b))
except Exception as e:
    print(e)
print("This is a important line")