# 11 23
a=4;b="4"
ee=[1,2,3]
c=[1,2,3]
print(a)

# In "is" we are referring to the same object and in "==" we are'nt referring to the same object.
print(a is b) #exact location of object in memory
print(a == b) #value

print(ee is c) #exact location of object in memory
print(ee == c) #value

a="bruh"#both constant pointing to the same memory location
b="bruh"#both constant pointing to the same memory location
print(a is b) #exact location of object in memory
print(a == b) #value
print()

# "==" compare the values and "is" operator compare the identity.

a=(1,2)
b=(1,2)
print(a is b) #exact location of object in memory
print(a == b) #value
print()
a=None
b=None
print(a is b) #exact location of object in memory
# print(a is a,"vgood") #exact location of object in memory
print(a is None,"vgood") #exact location of object in memory
print(a == b) #value
print()