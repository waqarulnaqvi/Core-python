"""bin method(Strings):
Creates a string from iterable objects(koi bhi esi cheez jisse iterable kiya ja sakta ho like lists,tuples etc)..

   l=["apple","mango","banana"]

",and,".join(l)

iterable objects like lists,tuples etc..
"""
# Tuple:
# l=("Camera","Laptop","Phone","ipad",'Hard Disk','Nvidia Graphic 3080 card')

# Lists:
l=["Camera","Laptop","Phone","ipad",'Hard Disk','Nvidia Graphic 3080 card']
# sentence= " and ".join(l)
# sentence= "~~".join(l)
# sentence= "==".join(l)
sentence= "\n".join(l)
print(sentence)
print(type(sentence))