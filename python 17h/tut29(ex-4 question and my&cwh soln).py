"""
# Exercise-3(Pattern Printing)
Input =Integer n
Boolean =True or False

True n=4
*
**
***
****

False n=4
****
***
**
*
"""
"""METHOD 1:"""
# n=int(input("How many times do you want to print * :"))
# bol=bool(input("For ascending order pattern enter any key for descending just enter:"))
# if bol==True:#you can also write 1 here.
#     for i in range (n):
#         for j in range(i + 1):
#             print(" * ", end="")
#         print()
# elif bol==False:
#     for i in range(n):
#         for j in range(n - i):
#             print(" * ", end="")
#         print()

"""METHOD 2:"""
def pattern ():
    n = int(input("How many rows do you want to print :"))
    bo = bool(int(input('''    For ascending order enter 1:
    For descending order enter 0:
    ''')))
    if bo is True:  # you can also write 1 here.
        for i in range(n):
            for j in range(i + 1):
                print(" *", end=" ")
            print()
    else:
        for i in range(n):
            for j in range(n - i):
                print(" *", end=" ")
            print()
    b=bool(int(input('''Do you want to continue:
    1 for yes
    0 for no
    ''')))
    if b is True:
        pattern()
    else:
        print("See you later :)")

pattern()
