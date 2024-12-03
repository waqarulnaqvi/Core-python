"""
# NOTE :You can use else statement with for and while loop..
# else with for and else with while are less use in python..
for loop:
A for loop is used to iterate through a sequence like list, tuple or string [iterables]

The synatx of a for loop looks like this:
l=[1,2,7]
for item in l:
    print(item)   ->print 1,7,8
"""
fruits=["Banana",'Watermelon',"grapes","Tomato","Gauava"]
# print(fruits[5])#Error..#IndexError: list index out of range
for item in fruits:
    print(item)