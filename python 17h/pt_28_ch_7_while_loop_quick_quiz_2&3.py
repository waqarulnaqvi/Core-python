"""
# NOTE :You can use else statement with for and while loop..
# else with for and else with while are less use in python..
i=0
while i<10:
    print("Yes "+str(i))
    print("Yes",i)#comma add space between the concatination..
    i=i+1

i=0
while i<5:
    print("Harry")
    i=i+1
"""

"""quick_quiz_2:
i=0
while i<50:
    print(i+1)
    i=i+1
"""    

"""quick_quiz_3:"""
fruits=["Banana",'Watermelon',"grapes","Tomato","Gauava"]
# print(fruits[5])#Error..#IndexError: list index out of range
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
else:
    print("This is inside else of while")       