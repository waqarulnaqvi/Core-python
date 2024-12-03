# Short hand if else
a=int(input("Enter a:\n"))
b=int(input("Enter b:\n"))
# Method :1
# if a>b : print("A is greater than B")
# else: print("B is greater than A")
# Method :2
if a>b : print("A is greater than B")
print("B is greater than A") if b>a else print("A and B are equal")
