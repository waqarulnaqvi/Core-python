"""
Dictionary:
Dictionary is a collection of key-value pairs..

Properties of a Python Dictionaries:
1)It is unordered.
2)It is mutable.#If you try to add more meaning of the (old world) than the value will be overriden and the old meaning of the world will be destroyed..
3)It is indexed.
4)cannot contain duplicate keys..
                 keys   values
                  |       |
Syntax : myDict={"key":"value",
                 "harry":"coder",
                  "list":[10,3,44]}
In most of the case keys ko lower case hi rakte hai..
"""
myDict={
"Fast":"In a Quick Manner",
"Fast":"In a Quickest Manner",#Fast meaning will be overriden in place of old meaning of the fast and the old meaning of the word fast will be destroyed ..
"harry":"Legend",
"Marks": [1,2,3],
"anotherdic":{"Zaman":"The girl who is less in height","Muslim":"Most Voilent people in the universe"},
1:2
}
# Dictionary Methods:
# print(myDict.keys())
# print(type(myDict.keys()))
# print(list(myDict.keys()))#temporary typecasting list to dictionary..#Prints the keys of the dictionary..
# print(type(myDict.keys()))
# print(myDict.keys())
# print(list(myDict.values()))#temporary typecasting list to dictionary..#Prints the values of the dictionary..
# print(myDict.values())#Prints the values of the dictionary..
# print(list(myDict.items()))#temporary typecasting list to dictionary..#Prints the (key, value) for all items/contents of the dictionary..
# print(myDict.items())#Prints the (key, value) for all items/contents of the dictionary..#dict_items is a kind of list..
print(myDict)
updateDict ={
    "Indian":"bhole log",
    "Waqarulrealfriends":0,
    "Waqarulfriends":"Alot of friends but it is a human tendency that people are selfish and animals are more friendly",
    0:False,
    True:23,
    11:"Hello have a good day",
    "Fast":"tezz/teja"#Fast meaning will be overriden in place of old meaning of the fast and the old meaning of the word fast will be destroyed ..
    
}
myDict.update(updateDict) #Update the dictionary by adding key-value pairs from updateDict..
print(myDict)

print(myDict.get("harry"))#prints value associated with key "harry"..
print(myDict["harry"])#prints value associated with key "harry"..

# The difference between .get and [] syntax in Dictionaries..
print(myDict.get("harry2"))#it will not throw an error if the harry2 is not present in the dictionary. it prints None..
# print(myDict["harry2"])#it will throw an error if the harry2 is not present in the dictionary..

# For more details about dictionary/dictionary_methods visit python official documentation on google..