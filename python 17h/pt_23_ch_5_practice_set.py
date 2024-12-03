"""Problem 1:
Dict={"dear":"प्रिय",
        "lust":"हवस",
     "english":"अंग्रेज़ी"}
# print(Dict)
print("Options are:",Dict.keys())
a=input("Enter the English word:")
print("Printing the meaning of your word is:")
# print(Dict[a])#it will throw an error if the key is not present in the dictionary..
print(Dict.get(a))#it will not throw an error if the key is not present in the dictionary. it prints None..
"""

"""Problem 2:
# Unique(non-repetative) elements means set ki baat ho rhi python me.. 
num1=int(input("Enter number 1:\n"))
num2=int(input("Enter number 2:\n"))
num3=int(input("Enter number 3:\n"))
num4=int(input("Enter number 4:\n"))
num5=int(input("Enter number 5:\n"))
num6=int(input("Enter number 6:\n"))
num7=int(input("Enter number 7:\n"))
num8=int(input("Enter number 8:\n"))
s={num1,num2,num3,num4 ,num5,num6,num7,num8}
print(s)

# An empty set can be created using the below syntax:
b=set()
# print(type(b))
# Adding elements in the empty set:
b.add(num1)
b.add(num2)
b.add(num3)
b.add(num4)
b.add(num5)
b.add(num6)
b.add(num7)
b.add(num8)
print(b)
"""

"""Problem 3:
s={18,"18",18.1}#because of the different different data type set will consider 18,"18" ,18.1 as an different elements..
print(s)
print(len(s))
"""

"""Problem 4:
s=set()
s.add(18)
s.add("18")
s.add(18.0)
print(s)
print(len(s))
"""

"""Problem 5:
# Important: This syntax will create an empty dictionary and not an empty set.. 
a={}
print(type(a))

# An empty set can be created using the below syntax:
a=set()
print(type(a))
"""

"""Problem 6 & 7:
dict={}
a1=input("Enter your favorite language chris:\n")
a2=input("Enter your favorite language henry:\n")
a3=input("Enter your favorite language charles:\n")
a4=input("Enter your favorite language harry:\n")
dict["chris"] =a1
dict['henry'] =a2
dict["charles"] =a3
dict["charles"] ="c"#Problem 7: Answer:latest updated value will be displayed.. 
dict['harry'] =a4
print(dict.keys())
print(list(dict.keys()))#temporary typecasting dictionary to list..
print(dict.values())
print(list(dict.values()))#temporary typecasting dictionary to list..
print(dict)
# print(False)
# print(True)
"""

"""Problem 8:
If languages of two friends are same.What will happen to the program in Problem 6?
it runs properly,yes dictionary can have the 2 same values to the 2 different keys and also dictionary does have more than 2 words have same meaning..
"""

"""Problem 9:"""
s={3,4,45,"harry",(1,2,3)}#run..#you can add tupple in the sets because you can not update tupple value. it is hashable..
# s={3,4,45,"harry",[1,2,3]}#Error..#you can not add list in the sets because list is unhashable it's value can be changed..
# s={3,4,45,"harry",{1,3,3}}#Error..
# s={3,4,45,"harry",{1:3}}#Error..#you can not add dictionary in the sets because dictionary is unhashable it's value can be changed..
# s[0]=34#Error..#TypeError: 'set' object does not support item assignment
print(s)