# List is the one of the most used data type in python.. 
# List slicing same as string slicing:
friends=['Me','Azaan',420,"Myself","Only me","Waqarul"]
print(friends[0:4])
print(friends[-4:])
''' List slicing:
           0      1     2     3        4        5 
friends=['Me','Azaan',420,"Myself","Only me","Waqarul"]
          -6     -5    -4    -3       -2       -1
 '''
print(friends[0:3])
print(friends[1:3])
print(friends[0:7])
print(friends[0:17])#run.. whole list will print..
print(friends[:4])
print(friends[0:])  
print(friends[:])

c=friends[-4:-1]

print(c)
print(friends[3:6])


d=friends[0:7:1]
print(d)
d=friends[0:7:2]
print(d)
d=friends[0:7:3]
print(d)