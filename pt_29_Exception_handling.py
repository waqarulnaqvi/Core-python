'killo'
"yellow"
# a=input("Enter the number:")
# print(f"Multiplication table of {a} is :")
# try:
#     for i in range(1, 11):
#         print(f"{a} X {i} = {i * int(a)}")
# except :
#     print("Invalid Input")
# """
# except Exception as e:
#     print(e)
#     print("Invalid Input")
# """
#
# 'We use Exception handling so that program should not to be halt or program should not to be stop.'
print(__doc__)
#
# print(f"\n\nIf you consider {a} as string then the output will be:")
# for i in range(1,11):
#     print(f"{a} X {i} = {i*a}")


# try:
#     a=int(input("Enter an integer :"))
#     b=[3,4]
#     print(b[a])
#     print(5/a)
# except IndexError:
#     print("Index Error") #handles (invalid literal for int() with base 10: 'qwqq')
# except ValueError:
#     print("Number entered is not an integer.") #handles (list index out of range)
# except :
#     print("Another Error.") #handles (division by zero).

try:
    a=int(input("Enter an integer :"))
    b=[3,4]
    print(b[a])
    print(5/a)
except Exception as a:
    print(a)