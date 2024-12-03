"""Problem:1
def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
         if(num2>num3):
            return num2
         else:
            return num3        

print("The value of the maximum is :",maximum(222,13,377))
"""

"""Problem:2
def farh(cel):
    return (cel *(9/5)) +32

print("The celcius value in Farhreheit is :",farh(45),"F")
"""

"""Problem :3
print("Hello,",end="")#by default end is a \n in python..
print('HYY')
"""

"""Problem :4
def sum_of_nat_rec(num):
  if(num==1):
    return 1
  else:
    return num + sum_of_nat_rec(num-1)  

num=int(input("Enter a number:"))
print(f"Sum of {num} natural number is : {sum_of_nat_rec(num)}")
"""

"""Problem :5
'''Method 1:(my logic)
num=int(input("Enter length of the pattern:"))
for i in range(num,0,-1):
    print("*"*(i))
'''
'''Method 2:(cwh logic)'''
num=int(input("Enter length of the pattern:"))
for i in range(num):
    print("*"*(num-i))
"""

"""Problem :6
def inch_to_cm(num):
    return num*2.54
num=int(input("Enter a number:"))
print(f"{num} inches is {inch_to_cm(num)} cms")
"""

"""Strip function:
Strip function in python is same as trimmed function in java.."""
# test="      Hello Waqarul, How are you?       "
# print(test)
# print(test.strip())

"""Problem :7
def remove_and_strip(str,word):
    newstr=str.replace(word,"")
    return newstr.strip()
test="      Hello Waqarul, How are you?       "
print(test)
print(remove_and_strip(test," are "))
print(remove_and_strip(test,"naqvi"))
"""

"""Problem :8"""
def mul_table(num):
    print("\nMultiplication table of",num,"is:")
    for i in range(1,11):
        # print(str(num)+ " X "+str(i)+" = "+str(i*num))
        # fstrings:
        print(f"{num} X {i} = {num*i}")
def mul_rev_table(num):
    print("\nMultiplication table of",num,"in reverse is:")
    for i in range(10,0,-1):
        # print(str(num)+ " X "+str(i)+" = "+str(i*num))
        # fstrings:
        print(f"{num} X {i} = {num*i}")

num=int(input("Enter the number:"))
mul_table(num)
mul_rev_table(num)

