"Assignment 15:"
# 2 20
# # Problem:1
# name="John Smith"
# print(name[1])
#
# # Problem:2
# print(name[-2])
#
# # Problem:3
# print(name[1:-1])
#
# # Problem:4
# print(len(name))
#
# # Problem:5
# print(f"{2+2}+{10%3}")

# Problem:6
# name="john smith"
# print(name.title())
#
# # Problem:7
# name="   john smith      "
# print(name.strip())
#
# # Problem:8
# name="john smith"
# print(name.find("Smith"))
#
# # Problem:9
# name="john smith"
# print(name.replace("j","k"))
#
# # Problem:10
# name="john smith"
# if "John" in name:
#     print("Yes ,john is in the name")
# else:
#     print("NO ,john is in the name")
#
# # Problem:11
# print(10**3)
#
# # Problem:12
# x=1
# x+=2
# print(x)
#
# # Problem:13
# print(10=="10")
#
# # Problem:14
# print("bag">"apple")
#
# # Problem:15
# print(not(True or False ))

# Problem:16
# for i in range(1, 10, 2):
#     print(i)

# Problem:17
# Name 3 iterable objects in Python.
# Lists,tuples,dictionaries and sets are all iterable objects

# Problem:18
def showcase(limit):
    for i in range(limit+1):
        if i%2==0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")

showcase(int(input("Enter the limit:")))

# Problem:19
# def show_star(n=5):
#     for i in range(n+1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# show_star()

# Problem:20
# inp=int(input("Enter the limit:"))
# for i in range(2,inp+1):
#     count=1
#     for j in range(2,inp//2):
#         if i%j ==0 and i!=j :
#            count=0
#            break
#     if count==1:
#         print(i,end="\t")


# Assignment 15
# Assuming (name = “John Smith”), what does name[1] return?
# What about name[-2]?
# What about name[1:-1]?
# How to get the length of name?
# What is the result of f“{2+2}+{10%3}”?
# Given (name = “john smith”), what will name.title() return?
# What does name.strip() do?
# What will name.find(“Smith”) return?
# What will be the value of name after we call name.replace(“j”, “k”)?
# How can we check to see if name contains “John”?
# What is the result of 10 ** 3?
# Given (x = 1), what will be the value of after we run (x += 2)?
# What is the result of 10 == “10”?
# What is the result of “bag” > “apple”?
# What is the result of not(True or False)?
# What does range(1, 10, 2) return?
# Name 3 iterable objects in Python.
# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# *
# **
# ***
# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.