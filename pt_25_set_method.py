# 9:15
s1={34,3,6,4,4,45}
# In set element order does'nt matters
s2={}#Empty dictionary
print(type(s2))
s2=set()#Empty set
print(type(s2))
s3={34678,6,4567}

print(s1.union(s3))
print(s1.intersection(s3))

# Union update:
s1.update(s3)#Insert those values in s1 which is not in s2
print(s1)

# Intersection Update:
a={3,2,4,5}
b={1,2,3,8}
a.intersection_update(b)
print(a)

print(a.isdisjoint(b))
"""Two set is said to be disjoined set if they partitioned in 2 non-empty set in such a way that it's one end in first set and other end in other set.
 eg: a={x1,y2,x3}
        |  |  |
     b={y1,x2,y3}
"""
"""To set said to be disjoined set if they have no element in common"""
x={1,2,3}
y={4,5,6}
print(x.isdisjoint(y))

# Symmetric difference:(Those values which are not common)
# A and B= (AUB) - (A^B)
# A and B= (A-B) U (B-A)
print(a.symmetric_difference(b))

# Symmentric Difference Update:
a.symmetric_difference_update(b)
print(a)

a={3,2,4,5}
b={1,2,3,8}
print(a.difference(b)) #the element which is only in a but not in b
print(b.difference(a))  #the element which is only in b but not in a

# Difference Update:
a.difference_update(b)
print(a)

# Superset:
city={"Tokiyo","Kabul","merat","mazaffar nagar"}
city2={"Tokiyo","Kabul"}
print(city.issuperset(city2))
print(city.issuperset(city))
print(city2.issubset(city),end="\n\n")

a={3,4,5}
b={4,8}
print(a.issubset(b))
print(b.issubset( a))
print(b.issubset( b),end="\n\n")

print(a.issuperset(b))
print(b.issuperset(a))
print(a.issuperset(a))

city.add("Yellow")
print(city)

# if you want to add more than 1 elements in a set you can use update method
city.update("kilo","pilo")
print(city)
city3={"dillo",2,23,32,None,True,False,'k','kk'}
city.update(city3)
print(city)

"""The main difference between remove and discard is that if element not present in a set discard does not raise an error but remove will raise an error."""
city.discard("e4rer")
print(city)
city.discard(False)
print(city)

city.remove('Tokiyo')
print(city)
# city.remove("WEWE")
# print(city)
print("Hello")

item=city.pop() #This method remove any random value.
print(city)
print(item)

# del:del is not a method,rather it is a keyword which deletes the set entirely.
# del city
# print(city)

# clear() method delete the all element of the set not the entire set
# city.clear()
# print(city)

# You can also use in keyword in a set
if "mazaffar nagar" in city:
    print("Yes")
else:
    print("NO")
