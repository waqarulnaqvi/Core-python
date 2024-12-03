# you can update lists but you can't update tuples..
"""Tuples in Python:
A tuple is an immutable(Cannot change) data type in Python.."""
# Creating a tuple using ()..
t=(1,2,4,5)
# t=(1,2,4,2,5) #Run.. print (1,2,4,2,5)
# Printing the elements of the tuple..
print(t)
print(t[3])
# Cannot update the value of the tuple it's hashable..
# Once defined a tuple's elements cannot be altered or manipulated..
# t[0]=34 #throws an error..#'tuple' object does not support item assignment..
t1=()#Empty tuple..
t3=(4)#Wrong way to declare a Tuple with single element..It's not a tuple it's a number..
t2=(2,)#Tuple with only one element needs a comma..
print(t1)
print(t2)
print(t3)