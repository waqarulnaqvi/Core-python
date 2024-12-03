# Assignment 7

# print(10/3 ,"\t",10//3)
#Answer 1: 10/3 returns 3.333333 instead of 3, 10//3 returns 3 instead of 3.33333

# Answer 2: result of 10**3 is 1000,
# print(10**3)

# Answer 3:x value will become 3

# Answer 4:By using round function round(value)
# print(round(35.8734))

#Answer 5: 1.0
# print(float(1))

# Answer 6:False
# print(bool(False))

# Answer 7:false
# print(10=="10")

# Answer 8:True
# print("bag">"apple")

# Answer 9:False
print(not(True or False))

# Answer 10:
# for i in range(1,10,2):
#     print(i)
# OUTPUT:
# 1
# 3
# 5
# 7
# 9

# Answer 11:
# print("The number which are divisible by 7 and are the multiple of 5 between 1500 and 2700 are as follows:")
# i=1500
# while i<=2700:
#     if i%7==0:
#         print(i)
#     i=i+5

# Answer 12:
# for i in range(1,6):
#    for j in range(i):
#        print("*",end="")
#    print()
#
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

# Answer 13:
# num=countev=countodd=0
# while True:
#     num=int(input(" Enter a numbers (-1 to stop the loop) :"))
#     if num==-1:
#         break
#     elif num%2==0:
#         countev=countev+1
#     else:
#         countodd=countodd+1
#
# print("Total even number is :",countev,"\nTotal odd number is :",countodd)

# Answer 14:
# for i in range(7):
#     if i==3 or i==6:
#         continue
#     print(i)

# Answer 15:
# age=int(input("Enter student age:"))
# if age >15 and age<18:
#     print("A Student can enroll into the college cricket club")
# else:
#     print("A Student can not enroll into the college cricket club")

# Answer 16:
# run=False
# if not run:
#    print("I am a not operator")

# Answer 17:
# inp=int(input("Enter a year:"))
# if inp%400==0 and inp%100==0:
#     print(f"{inp} is a leap year")
# elif inp%4==0 and inp%100!=0:
#     print(f"{inp} is a leap year")
# else:
#     print(f"{inp} is not a leap year")

# Answer 18:
# pattern=["*****"," *   *"," *   *"," ****"," *"," *"," *"]
# for p in pattern:
#     print(p)