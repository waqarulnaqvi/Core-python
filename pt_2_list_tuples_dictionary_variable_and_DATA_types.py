# In python everything is object../
# Built in datatypes in python
a=3 #int
b=-34.343 #float
c=complex(6,2) #complex :6 +2i
print(a)
print(b)
print(c,end="\n\n")

"""LIST,TUPLES AND,DICTIONARY"""
# list is a collections of different data elements
list=[8,2.3,[-4,5],["apple","banana"],True,False,None]
print(list,end="\n\n")
list1=[8,2.3,[-4,5],["apple","banana"],True,False,None]
print(list1,end="\n\n")
# list is mutable or changeable
# tuples is immutable
# dictionary is a collection of key value pair
# dictionary is a map data

tuple=(("parrot","sparrow"),("lion","Tiger"))
print(tuple,end="\n\n")

dict={"name":"Sakshi","age":20,"canVote":True,1:"bodycount",True:"beauty",False:"anger issues",0:"chutiyapa",34:33}
print(dict["name"])
print(dict["age"])
print(dict[1])
print(dict[True])
print(dict[False])
print(dict[34])
print(dict,end="\n\n")


a=1
print(type(a))
print(a,sep="23")
print(a,34,sep="23")

a="Harry"
print(type(a))
print(a)

a=True
print(type(a))
print(a)

a=None
print(type(a))
print(a)

