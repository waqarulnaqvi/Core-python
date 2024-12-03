# the difference between list and tuples is that tuples is immutable.
# Tuples are used to create constant list.
"""
 positive index in tuple : 0  1  2 3  4
                    tuple=(23,23,2,2,32)
 negative index in tuple :-5 -4 -3 -2 -1
"""
# tuple and list both supports negative as well as positive indexing.
tup=(2,2,12,"Green",True)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
print(len(tup))
print(tup[len(tup)-1])
print(tup[-1])
# print(tup[-11])#IndexError: tuple index out of range
# print(tup[32]) #IndexError: tuple index out of range
print(type(tup),tup)
# tup(2) # Error because python Interpretor get confused.
tup=(2,)  # one value tuple when declared must be separated by comma otherwise python Interpretor get confused.
print(type(tup),tup)
# tup[0]=12 #Error because it can not be changeable.
if 2 in tup: # in keyword is used in both tuple and list
    print("2 is present ")
else:
    print("2 is not present")


# same as list tuple slicing also possible
# tuple slicing
tup=(12,2,4,4,3,534,334,)
print(tup[0:3])
print(tup[0:])
print(tup[0::2])
tup=tup[1:5:2]#tuples are immutable same as string tuple object refrence only updated it's value can not be changed
#tuples are immutable ,strings are immutable and,list are mutable.
print(tup)
print(tup)