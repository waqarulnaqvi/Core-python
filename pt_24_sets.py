# In set element order does'nt matters
# In python every thing is an object
s={2,3,4,3,44}
print(s)

info={"Carla",19,False,5.9,19}
print(info)

#Try to create an empty set check using a type function whether the type of a variable is a set or not
kk=12121


harry={} # it makes an dictionary but not a set. #Empty dictionary
print(type(harry))
print(harry)

harry=set()#Empty set
print(type(harry))

for value in info:
    print(value)