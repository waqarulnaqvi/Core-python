# Question:1
inp=input("Enter a value:")
if inp.isdigit():
    print("It is a number")
else:
    if inp.isupper():
        print("It is in uppercase")
    elif inp.islower():
        print("It is in lowercase")
    elif inp.casefold():
        print("Studly caps or sticky caps")

# Question:2
# inp=input("Enter a value:")
# if inp=="QUIT":
#     print("Quiting from the loop")
#     exit()
# print("Length of a String is ",len(inp))

#Question:3
# num=countev=countodd=sumev=sumod=0
# while True:
#     num=int(input("Enter a numbers :"))
#     if num==-1:
#         break
#     elif num%2==0:
#         sumev+=num
#         countev=countev+1
#     else:
#         sumod+=num
#         countodd=countodd+1
# if sumev!=0:
#     print("Sum of even number is:", sumev, "\nAverage of even number is:", sumev / countev, "\n")
# if sumod!=0:
#     print("Sum of odd number is:", sumod, "\nAverage of odd number is:", sumod / countodd, "\n")

# Question:4
# a,b=input("Enter a floating point number and an integer:").split()
# if float(a) >4.14:
#    print("Integer number is :",int(b) +10)
# else:
#     print("Integer number is :",int(b))

#Question:5
# def percentage(sub=5):
#     sum=i=0
#     while i<sub:
#         subj =int(input(f"Enter {i+1} subject marks :"))
#         sum=sum+subj
#         i=i+1
#     return sum/sub
#
# print("Enter X marks :")
# X=percentage()
# print("X percentage is :",X)
#
# XIIstream=input("\nChoose Stream :pcm)Science ca)Commerce and arts :")
# print("Enter XII marks :")
# XII=percentage()
# print("XII percentage is :",XII)
#
# grastream=input("\nChoose Stream :pcm)Science ca)Commerce and arts :")
# print("Enter graduation marks :")
# gra=percentage()
# if grastream!=XIIstream:
#     gra=gra-5
# print("Graduation percentage is :",gra)
#
# if X>=80 and XII>=80 and gra>=70:
#     print("You are eligible for PG course")
# else:
#     print("You are not eligible for PG course")

# Question:6
# unit=int(input("Enter unit consumption:"))
# if unit <=150:
#     print("Electricity bill is:",3*unit)
# elif unit>=151 and unit<=350:
#     bill=100+(unit-150)*3.75
#     print("Electricity bill is:",bill)
# elif unit>=351 and unit<=450:
#     bill=250+(unit-350)*4.25
#     print("Electricity bill is:",bill)
# else:
#     bill=400+(unit-600)*5
#     print("Electricity bill is:",bill)



