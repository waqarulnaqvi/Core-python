# Exercise-3 Guess the number.
# no. of guesses.
# print no. of guesses left.
# no. of guesses he took to finish.
# when all the guesses will be finished then print game over.
import random
"""
# All the values will be print in 0.something.
num =random.random()
print(num)
result:0.6008687917234723
# All values will be print in 1.something &,2.something and so on.
num =random.uniform(1,10)
print(num)
result:1.5911692152196013
"""
# print(__doc__) print none.
num =random.randint(1,20)
print("Guess the number, the number is between (1 to 20)")
print("you have only 5 choices:")
i=1
while i<=5:
    num_1=int (input("Enter a number: "))
    if num_1==num:
        print("Absolutely Correct \n")
        break
    print("YOUR NUMBER IS GREATER " ) if num_1>num else print("YOUR NUMBER IS LESSER ")
    # Method 1:
    # print('no. of choices left ',5-i,"\n" )
    # Method 2:
    # print('no. of choices left ', 5 - i, '''
    #    ''')
    # print('no. of choices left ', 5 - i, """
    #     """)
    # Method 3:
    print(f"no. of choices left {5 - i}\n")
    i+=1
print("Number choose by Computer is:",num)
