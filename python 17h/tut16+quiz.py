"""Tuple"""
# list=["harry","larry","karry","Marie"]
# tuple=("harry","larry","karry","Marie")
# for items in tuple:
# print(items)
"""list"""
# list=[["harry",2],["larry",77],["karry",5],["Marie",3]]
# for items,lollypop in list:
#    print(items,"and",lollypop)#this is how you can unpack any list..
"""Dictonary"""
# list = [["harry", 2], ["larry", 77], ["karry", 5], ["Marie", 3]]
# dict = dict(list)
# for items, lollypop in dict.items():
#        print(items, "and", lollypop)  # this is how you can unpack any list..
# print(dict)
"""if you want only key then you can right in this method dictonay."""
# for items in dict:
#        print(items)
"""quiz"""
list=["harry","larry","karry","Marie",88,99,4,898,7,5]
for item in list:
   if str(item).isnumeric() and item>6:
    print(item)