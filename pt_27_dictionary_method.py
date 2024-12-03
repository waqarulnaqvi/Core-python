'''set elements are unordered in python but dictionary are ordered in python that means we get the same ordered key when we again and again update the dictionary.'''
print(__doc__)
ep={1:45,2:121,1:1212,3:1212}
print(ep.items())
ep2={4:232,8:2323}
ep.update(ep2)
print(ep.items())

# ep.clear() # clear method is used to clear the dictionary.
# print(ep.items())
# print(ep)

# ep.pop(11) # If
#If the corresponding key is not present than pop method will throw an error.
# ep.pop(1)
# print(ep)
# ep.popitem()# it remove the last  key & value of the dictionary.
# print(ep)
# ep.popitem()# it remove the last key & value of the dictionary.
# print(ep)

# del ep #it delete the dictionary
# print(ep)

# del ep[1]#If the corresponding key is not present than pop method will throw an error.
# If key is not provided, then the del keyword will delete the dictionary entirely.
# del ep["2"] #It will also throw an error because 2 is present in the dictionary as an Integer but you are deleting "2" as an string.
del ep[2]
print(ep)
print("hello")





