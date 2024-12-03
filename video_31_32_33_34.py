tup=("parrot","sparrow",("lion","Tiger"))
print(tup,end="\n\n")
print(len(tup))
print(tup[len(tup)-1])
print(tup[-1])

# you can only change tuples indirectly by converting it into the list than convert it back to the tuple but directly you can not change the tuple however you can concatinate the tuple.
countries =("Spain","Italy","India", "England", "Germany ")
temp=list(countries)
temp.append("Russia")
print(countries,type(countries))
print(temp,type(temp))
temp.pop(3)
temp[2]="Finland"

countries2=("gorakpur","Ramgadh","Sitapur")
Asiancountries=countries+countries2
print(Asiancountries)
print(countries.count(3))
res=countries.count("Spain")
print(res)
res=countries.count("spain")
print(res)
print(len(countries))
# print(countries.index(3))# Error because 3 is not in the tuple
print(end="\n\n")
print(countries.index("Finland",0,4))
# print(countries.index("finland",0,4))#it raise value error if the value is not in the tuple.
#we use camel case naming convention in list and tuples name so it starts with small letter.
#you can use all the method of the list when you convert tuple it into the list and make sure to convert it back into the tuple.

