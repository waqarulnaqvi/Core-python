# 90 percent cases me aap list comprehensions hi use karenge or 10 percent cases me hi aap koi or comprehensions (like dictionary and,sets etc) use karenge..

# set_comprehensions:
# t=[2,3,44,55,64,22,11,3,5,7,9,223,22]#both are correct gives the same output..
t={2,3,44,55,64,22,11,3,5,7,9,223,22}#both are correct gives the same output..
s={i for i in t}
print(s)


# a ={2,3,44,55,64,22,11,3,5,7,9,223,22}#both print different output non-repetative element won't print because set is created..
a =[2,3,44,55,64,22,11,3,5,7,9,223,22]#both print different output non-repetative element print because list is created..
# Method:1
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)        

# Method:2(Shortcut to write the same)
# List_Comprehensions:
b=[i for i in a if i%2==0]
print(b)    

b=[item for item in a if item>8]
print(b)    