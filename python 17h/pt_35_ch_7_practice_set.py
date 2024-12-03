"""Problem 1:
num=int(input("Enter the number:"))
print("\nMultiplication table of",num,"is:")
for i in range(1,11):
    # print(str(num)+ " X "+str(i)+" = "+str(i*num))
    # fstrings:
    print(f"{num} X {i} = {num*i}")
"""

"""Problem 2:
l1=["Harry","Sohan","Sachin","Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello "+name)
"""

"""Problem 3:
num=int(input("Enter the number:"))
print("\nMultiplication table of",num,"is:")
i=1
while i<=10:
    # print(str(num)+ " X "+str(i)+" = "+str(i*num))
    # fstrings:
    print(f"{num} X {i} = {num*i}")
    i=i+1
"""

"""Problem 4:
num=int(input("Enter the number:"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
   print("Number is prime")
else:
    print("Number is not prime")
"""

"""Problem 5:
num=int(input("Enter the number:"))
sum=0
for i in range (num):
   sum+=(i+1)
print("The sum of natural number till",num,"is :",sum)   
"""

"""Problem 6:
# n!= 1X2X3X4.....Xn
num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
# print("The factorial of ",num,"is :",fact)   
print(f"The factorial of  {num} is : {fact}")   
"""

"""Problem 7:
n=4
for i in range(4):
    print(" " *(n-i-1),end="")
    print("*" *(2*i+1),end="")
    print(" " *(n-i-1))
"""

"""Problem 8:
n=4
for i in range(4):
    print("*"*(i+1))
"""

'''Problem 9:'''
"""Method:1
n=3
for i in range(n):
    if(i==1):
        print("*"*i,"*"*i)
    else:
        print("*"*n)
"""
"""Method:2"""
n=5
for i in range(n+1):
    if(i>0 and i<n):
        print("*"+" "*(n-1)+"*")
    else:
        print("*"*(n+1))
        

"""Problem 10:Multiplication table in reverse order:
num=int(input("Enter the number:"))
print("\nMultiplication table of",num,"in reverse is:")
for i in range(10,0,-1):
    # print(str(num)+ " X "+str(i)+" = "+str(i*num))
    # fstrings:
    print(f"{num} X {i} = {num*i}")
"""
