# Dictionary is nothing just a combination of key value pair.
dict ={}
# print(type(dict)) #Empty dictionary

set =set()
# print(type(set)) #Empty set

# Non dictionary is ordered .On python 3.7 onward dictionary become ordered before 3.7 version dictionary is unordered in python.
dict={"Waqarul":"Productive person","Spoon":"Non living thing" ,1:"Azaan"}
print(dict)#dictionary is ordered means if you print the keys of the whole dictionary they always make an order.
dict["yell"]=2
dict["ball"]="ktm"
print(dict)
print(dict["ball"])
dict["yell"]+=2
# dict["Waqarul"]=1
print(dict)
print(dict["Waqarul"])#Same
print(dict.get("Waqarul"),end="\n\n")#Same

# print(dict[1])#Same
# print(dict.get(1))#Same
#
# print(dict.get(232))# it does not gives an error if key value is not present in the dictionary if print "None.
# # print(dict[232])# it gives an error if key value is not present in the dictionary.
# print(dict.values())#it give all the dictionary values.
# print(dict.keys(),end="\n\n")#it give all the dictionary keys.
#
# for key in dict.keys():
#     print(key)
# print()
#
# for key in dict.keys():
#     print(dict[key])
# print()
#
# for value in dict.values():
#     print(f"The value corresponding to the key is :{value}")
# print()
#
# txt="The value corresponding to the key is :{}"
# for value in dict.values():
#     print(txt.format(value))
# print()
#
# txt="The value corresponding to the key is :{value}"
# for value in dict.values():
#     print(txt.format(value=value))
# print()
#
# txt="The value corresponding to the key is :{vaalue}"
# for value in dict.values():
#     print(txt.format(vaalue=value))
# print()
#
# # Dictionary is used to create for a mapping
# print(dict.items())
# for key,value in dict.items():
#     print(f"The value corresponding to the key {key} is {value}")
# print(end='\n\n')
#
# for key,value in dict.items():
#     print("The value corresponding to the key {key} is {value}".format(key=key,value=value))
# print(end='\n\n')
#
# for key,value in dict.items():
#     print("The value corresponding to the key {1} is {0}".format(value,key))
# print(end='\n\n')
#
# for key,value in dict.items():
#     print("The value corresponding to the key {} is {}".format(key,value))
# print(end='\n\n')
#
