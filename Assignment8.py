# 12 7
# Assignment 8

# Answer 1:
# import math
# inp=int(input("Enter n number :"))
# for i in range(1,inp+1):
#     print(math.pow(5,i))

# Answer 2:
# import math
# inp=int(input("Enter n number :"))
# print("Using while loop:")
# i=1
# while i!=inp+1:
#     print(math.pow(i,2))
#     i=i+1
#
# print("\nUsing for loop:")
# for i in range(1,inp+1):
#     print(math.pow(i,2))

#Answer 3:
# sum=0
# for i in range(501):
#     if i%5==0:
#         sum = sum + i
#         print("Sum is :",sum)
#     else:
#         sum=sum+i

#Answer 4:
# no =37.4847889
# count=0
# while no!=int(no):
#     count=count+1
#     no=no*10
    # # print("Float is :",no)
    # # print("Integer is :",int(no))

#Answer 5:
# print(count)

#Answer 6:
# inp=int(input("Enter a number:"))
# count=0
# for i in range(2,(inp//2)+1):
#     if inp%i==0:
#         print("Not a prime number")
#         count=1
#         break
#
# if count==0:
#     print("Prime number")



# Answer 7:
# for i in range(1,6):
#     print(f"Multiplication table of {i} is :")
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")
#     print()

# Answer 8:
# sum=0
# for i in range(1,21):
#     if i%2!=0 or i%3!=0 or i%5!=0:
#         sum=sum+i
#
# print("Sum is :",sum)

# Answer :9
# from math import pow
# inp=int(input("Enter a number:"))
# len=sum=0
# n=inp
# while inp!=0:
#     len=len+1
#     inp=inp//10
# inp=n
# while inp!=0:
#     rem=inp%10
#     sum=sum+pow(rem,len)
#     inp=inp//10
#
# if sum == n:
#     print("Amstrong Number")
# else:
#     print("Not an Amstrong Number")


