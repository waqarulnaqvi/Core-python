#exercise 2- faulty calculator
#45+3=555,56+9=77,56/6=4
#Design the calculator which will correctly solve all the problems except the followings ones:
#45+3=555,56+9=77,56/6=4
#your program should take operator and the two numbers as input from the user and then return the result.
print("press \"1\" for Addition \"2\" for Multiplication \"3\" for Substraction \"4\" for Divison ")
inp=int(input())
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
if inp==1:
    # num = input("enter first number")
    # b = input("enter second number")
    if num1==45 and num2==3 or num1==3 and num2==45:
        print("555")
    elif num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("77")
    else:
      print(num1+num2)
elif inp==2:
    print(num1 * num2)
elif inp==3:
    print(num1 - num2)
else:
    if num1 == 56 and num2 == 4 :
       print("4.0")
    else:
        print(num1 / num2)

