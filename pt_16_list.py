l=[3,3,2]
print(l)
print(type(l))
# ek naame ke under agar hum bhut si cheez python me print karana chahte hai to list ka istemaal karte hai.
marks=[32,33,32,"STring",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5]) #IndexError: list index out of range
# list is a ordered collection of data items.
# list are changeable meaning we can alter them after creation.

"""    
 positive index in list : 0  1  2 3  4
                    list=[23,23,2,2,32]
 negative index in list :-5 -4 -3 -2 -1 
"""
# cwh avoid using negative indexing.
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if 32 in marks:
    print("Yes")
else:
    print("No")

if 33 in marks:
    print("Yes")
else:
    print("No")

if 3 in marks:
    print("Yes")
else:
    print("No")

# we compare list as well as string using for loop
if "HA" in "HArry":
    print("YES")

if "ha" in "HArry":
    print("YES")
else:
    print("no")

print(marks)
print(marks[:])#same
print(marks[0:len(marks)])#same
print(marks[1:-1])
print(marks[1:5-1])
print(marks[1:5-1:2])# last index where 2 is placed is called jump index.

#list comprehension
lst=[i for i in range(10)]
print(lst)
lst=[i*i for i in range(10)]
print(lst)

lst=[i*i for i in range(10) if i%2==0]
print(lst)

names=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0 =[item for item in names if "o" in item]
print(namesWith_0)

ames=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0 =[item for item in names if (len(item)>4)]
print(namesWith_0)

names=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0 =[item for item in names if "a" in item]
print(namesWith_0)

names=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0 =[item for item in names for k in item if k!="a" ]
print(namesWith_0)

names=["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_0 =[item for item in names if "a" in item ]
print(namesWith_0)

