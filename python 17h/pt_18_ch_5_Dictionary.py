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
"Harry":"Legend",
"Marks": [1,2,3],
"anotherdic":{"Zaman":"The girl who is less in height","Muslim":"Most Voilent people in the universe"}
}
# print(myDict['fast'])
print(myDict['Fast'])#print "In a Quickest Manner"..
print(myDict["Harry"])
# print(myDict['Harr'])#Throws Error if key is not in the dictionary..
print(myDict['Marks'])
myDict['Marks']=[34,34]#it is mutable you can change micDict marks value..
print(myDict["Marks"])
print(myDict["anotherdic"]["Muslim"])

