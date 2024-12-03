# class CustomError(Exception):
#     pass
#
# try:
#     pass
# except CustomError:
#     pass
#
# a=int(input("Enter any value between 5 and 9 :"))
# if(a<5 or a>9):
#     raise ValueError("value should between 5 and 9")

'quick quiz'
a=input("Enter any value between 5 and 9 :")
# if not(a=="quit"):
#     print("Invalid string")
if (a=="quit"):
    print("ohk")
elif(int(a)<5 or int(a)>9):
    raise ValueError("value should between 5 and 9")