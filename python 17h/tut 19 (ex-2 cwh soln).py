"""
Exercise 2- faulty calculator
45+3=555,56+9=77,56/6=4
Design the calculator which will correctly solve all the problems except the followings ones:
45+3=555,56+9=77,56/6=4
your program should take operator and the two numbers as input from the user and then return the result.
"""
# def calculator():
#     print("WELCOME TO WAQARUL'S CALCULATOR")
#     num1 = int(input("enter first number :"))
#     num2 = int(input("enter second number :"))
#     inp = input('''
#         press + for Addition,
#         * for Multiplication,
#         - for Substraction,
#         / for Divison ,
#         ** for power &,
#         % for modulus''')
#     if inp == "+":
#         if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
#             print("45+3=555")
#         elif num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
#             print("56+9=77")
#         else:
#             print(f"{num1}+{num2}={num1+num2}")
#     elif inp == "*":
#         print(f"{num1}*{num2}={num1*num2}")
#     elif inp == "-":
#         print(f"{num1}-{num2}={num1-num2}")
#     elif inp =="**":
#         print(f"{num1}**{num2}={num1**num2}")
#     elif inp =="%":
#         print(f"{num1}%{num2}={num1%num2}")
#     elif inp =="/":
#         if num1 == 56 and num2 == 4:
#             print("56/4=4.0")
#         else:
#             print(f"{num1}/{num2}={num1/num2}")
#     else:
#          print("you enter a Invalid key:")
#     again()
# def again():
#     cal_again=input("do you want to continue type y for yes and n for NO:-")
#     if cal_again=="y":
#         calculator()
#     elif cal_again=='n':
#         # exit()
#         print("See you Later")
#         # exit()
#         # again()
#     else:
#         again()
#
# calculator()
print("WELCOME TO WAQARUL'S CALCULATOR")
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

def inputt():
    num1 = int(input("enter first number :"))
    num2 = int(input("enter second number :"))
    calculator()
def calculator():
    inp = input('''
         press + for Addition,
         * for Multiplication,
         - for Substraction,
         / for Divison ,
         ** for power &,
         % for modulus''')
    if inp == "+":
        if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
            print("45+3=555")
        elif num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
            print("56+9=77")
        else:
            print(f"{num1}+{num2}={num1+num2}")
    elif inp == "*":
        print(f"{num1}*{num2}={num1*num2}")
    elif inp == "-":
        print(f"{num1}-{num2}={num1-num2}")
    elif inp =="**":
        print(f"{num1}**{num2}={num1**num2}")
    elif inp =="%":
        print(f"{num1}%{num2}={num1%num2}")
    elif inp =="/":
        if num1 == 56 and num2 == 4:
            print("56/4=4.0")
        else:
            print(f"{num1}/{num2}={num1/num2}")
    else:
         print("you enter a Invalid key:")
    again()
def again():
    cal_again=input("Do you want to continue type y for yes and n for NO:-")
    if cal_again=="y":
        sameoperation()
        calculator()
    elif cal_again=='n':
        print("See you Later")
        # exit()
    else:
        again()

def sameoperation():
    k= input('''Do you want to use same operants  
               y for yes and 
               n for NO:''')
    if k=="y":
        calculator()
    elif k=="n":
        inputt()
    else:
        sameoperation()

calculator()
