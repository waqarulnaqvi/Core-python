# An empty set can be created using the below syntax:
a=set()
# print(type(a))
# Adding elements in the empty set:
a.add(5)
a.add(4) 
a.add(4)
a.add(42)
a.add(5)
#Adding a value repeatedly does not changes a set..
# a.add([4,3,5]) #you can not add list in the sets because list is unhashable it's value can be changed..
a.add((4,3,5)) #you can add tupple in the sets because you can not update tupple value. it is hashable..
# a.add({4:8}) #you can not add dictionary in the sets because dictionary is unhashable it's value can be changed..
# print(a)
# print(len(a))#Prints the length of this set..

# a.remove(5)# Removes 5 from the set..
# print(a)
## a.remove(15)#Error because 15 is not in the set..
# print(a)

# pop removes the 1 element from the first index..
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)

# a.clear()
# print(a)

# Union and Intersection function of the set:
b={1,2,3,4,5,6}
c={1,2}
print("Set a is :",a)
print("Set b is :",b)
print("Set c is :",c)
print("Union set a and b",a.union(b))
print("Intersection set a and b",a.intersection(b))

print("Union set a and c",a.union(c))
print("Intersection set a and c",a.intersection(c))

# For more details about sets/sets methods visit python official documentation on google..
