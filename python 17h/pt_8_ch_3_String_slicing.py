from traceback import print_tb


name="Waqarul"
"""print(name[0])
print(name[-2])
# name[0]='3' #Error you can not change string index value..

# String Slicing:
slicing='''0 1 2 3 4 5 6 
           W a q a r u l
          -7-6-5-4-3-2-1
           Here W a q a r u l =Waqarul for better readibility..'''
print(name[0:3])#last index is excluded..
print(name[1:3])#last index is excluded..
print(name[0:7])#last index is excluded..
print(name[0:17])#run.. #print the whole string..
print(name[:4]) # is same as name[0:4]..
#minimum non negative number is 0.
print(name[0:]) # is same as name[0:7].. 
print(name[:]) # is same as name[0:7].. 
# negative index is very useful when we don't know the actual length of the string..
c=name[-4:-1]# is same as name[3:6]..
# last index is excluded..#in this case -1 will be excluded..
print(c)
print(name[3:6])"""

# String Slicing with skip value:
d=name[0:7:1]#it skip nothing..
print(d)
d=name[0:7:2]#it skip 1 character..
print(d)
d=name[0:7:3]#it skip 2 character..
print(d)
