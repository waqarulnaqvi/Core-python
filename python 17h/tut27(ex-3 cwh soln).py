# Exercise-3 Guess the number.
# no. of guesses.
# print no. of guesses left.
# no. of guesses he took to finish.
# when all the guesses will be finished then print game over.

"Method :1"""
# num=13
# win= False
# print("Guess the number, the number is between (1 to 20)")
# i=1
# # while win: #by default true
# while not win:
#     num_1=int (input("Enter a number: "))
#     if num_1==num:
#         print("Absolutely Correct ")
#         print(f'''you uses {i} choice
#         \"GAME OVER\"''')
#         win=True
#     # Method:1
#     # elif num_1 > num:
#     #     print("YOUR NUMBER IS GREATER ")
#     # else :
#     #     print("YOUR NUMBER IS LESSER ")
#     # Method:2
#     else: print("YOUR NUMBER IS GREATER \n") if num_1 > num else print("YOUR NUMBER IS LESSER \n")
#     i+=1

"""Method 2:"""
# num=13
# print("Guess the number, the number is between (1 to 20)")
# print("you have only 5 choices:")
# i=1
# while i<=5:
#     num_1=int (input("Enter a number: "))
#     if num_1==num:
#         print("Absolutely Correct ")
#         print(f"you uses {i} choice")
#         exit()
#     # Method:1
#     # elif num_1 > num:
#     #     print("YOUR NUMBER IS GREATER ")
#     # else :
#     #     print("YOUR NUMBER IS LESSER ")
#     # Method:2
#     else: print("YOUR NUMBER IS GREATER ") if num_1 > num else print("YOUR NUMBER IS LESSER ")
#     # Method 1:
#     # print('no. of choices left ',5-i,"\n" )
#     # Method 2:
#     # print('no. of choices left ', 5 - i, '''
#     #    ''')
#     # print('no. of choices left ', 5 - i, """
#     #      """)
#     # Method 3:
#     print(f"no. of choices left {5 - i}\n")
#     i+=1
#
# # if  i<=6:
# # if  i<7:
# if  i==6:
#     print("GAME OVER")

"""Method 3:"""
num=13
print("Guess the number, the number is between (1 to 20)")
print("you have only 5 choices:")
for i in range(5):
    # print(i)
    num_1 = int(input("Enter a number: "))
    if num_1 == num:
        print("Absolutely Correct ")
        print(f"you uses {i+1} choice")
        exit()
    elif num_1 > num:
        print("YOUR NUMBER IS GREATER ")
    else:
        print("YOUR NUMBER IS LESSER ")

    if i<=3:
        print('no. of choices left ', 5 - (i + 1), '''
                   ''')
    else:
        print("NO CHOICES LEFT")

if  i<7:
    print("GAME OVER")