# Python me hrr cheez object hoti hai..
""" Problem 1:
# i=0
# myFruitList=[]
# while i<7:
#     f1=input("Enter Fruit ")
#     myFruitList[i]=f1
#     i+=1
# print(myFruitList)

f1=input("Enter Fruit number 1:")
f2=input("Enter Fruit number 2:")
f3=input("Enter Fruit number 3:")
f4=input("Enter Fruit number 4:")
f5=input("Enter Fruit number 5:")
f6=input("Enter Fruit number 6:")
f7=input("Enter Fruit number 7:")
myFruitList=[f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)
print(myFruitList[0])
print(myFruitList[3])
print(myFruitList[-3])
# print(myFruitList[20])#Error..#IndexError: list index out of range..
# lists can have repetative values...
"""

""" Problem 2:
m1=int(input("Enter Marks for Student number 1:"))
m2=int(input("Enter Marks for Student number 2:"))
m3=int(input("Enter Marks for Student number 3:"))
m4=int(input("Enter Marks for Student number 4:"))
m5=int(input("Enter Marks for Student number 5:"))
m6=int(input("Enter Marks for Student number 6:"))

myList =[m1,m2,m3,m4,m5,m6]
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
"""

"""Problem 3:
a=(2,34,33,"hello",34,False,True)
# a[0]=3434 #Error.. #TypeError: 'tuple' object does not support item assignment
print(a)
"""

"""Problem 4:
a=[3,34,4,34,22.4,False,]#Run..
print(a[0]+a[1]+a[2]+a[3]+a[4]+a[5])#Run..
print(sum(a))#Run..
a=[3,34,4,34,"Waqarul"]
print(a[0]+a[1]+a[2]+a[3])
# print(sum(a))#Error..#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Cannot use sum function on String..
a=['naqvi','Waqarul','azaan','Alpha male']
print(a[0]+a[1]+a[2]+a[3])
# print(sum(a))#Error..#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Cannot use sum function on String..
"""

"""Problem 5:"""
# Creating a tuple using ()..
t=(1,2,4,5,1,1,1,1)
print("Using Count Function:")
print(t.count(1))
print(t.count(3))
print(t.count(2))

print("Using Index Function:")
print(t.index(1))
# print(t.index(3))#Error..#ValueError: tuple.index(x): x not in tuple
print(t.index(2))
print(t.index(5))



