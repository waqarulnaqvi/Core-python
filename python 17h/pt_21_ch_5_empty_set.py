# Important: This syntax will create an empty dictionary and not an empty set.. 
a={}
print(type(a))

# An empty set can be created using the below syntax:
a=set()
print(type(a))
# Adding elements in the empty set:
a.add(5)
a.add(4)
a.add(4)
a.add(42)
a.add(5)
print(a)