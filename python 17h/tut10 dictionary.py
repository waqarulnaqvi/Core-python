# Dictionary :is nothing but keyvaluepairs(means word meaning)
# Dictionary is a case sensitive.
# d1=[1] list
#d1=(2,)tupples
#d1={"errter":"don"}dictionary
#d1={}
# print(type(d1))
d2={"azaan":"diet","zaman":"kuch ni","waqarul":"game","tazeen":{"body":"very small","height":"5ft","weight":"-33"} }
#dictionary is case sensitive..
#tazeen ki key value jo hai wo dictionary,tupple,list bhi ho sakti hai..
#your key value should bhi immutable..
print(d2["tazeen"]["weight"])
del d2["tazeen"]
# d2["444"]=8888
# d2[244]="fun"
# print(d2)
# del d2[244]
# del d2["444"]
# del d2["waqarul"]
# print(d2)
## d3=d2 d3 is a refernce of d2 ,d3 is not a new dictionary..
d3=d2.copy();#shallow copy
del d3["azaan"]
print(d2)
print(d3)
#get one value
print(d2.get("azaan"))
print(d2["azaan"])
#update function
d2.update({"aaa":"ygygy"})
d2[244]="fun"
print(d2)
print(d2.keys())
print(d2.items())#.items print key value pairs
# if you want to see additional fuction of python then go to the google and search "dictionary function python"..