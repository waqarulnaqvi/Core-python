# Python 3.5 does not have a f string ..f string is introduced in python 3.6..

# Before f string introduction ,we use format method which uses in place of f string.. 

name="Harry"
channel="CodeWithHarry"
# f string:
a=f"This is {name}.."
# format method:
a1="This is {}..".format(name)
a2="This is {} and his channel is {}..".format(name,channel)
a3="This is {} and his channel is {}..".format(channel,name)
a4="This is {1} and his channel is {0}..".format(channel,name)
# a5="This is {} and his channel is {}..".format(name)
# a6="This is {} and his channel is {0}..".format(name)#Error
# a7="This is {1} and his channel is {0}..".format(name)#Error
a8="This is {0} and his channel is {0}..".format(name)
a9="This is {0} and his channel is {1}..".format(name,channel)
# a10="This is {0} and his channel is {}..".format(name,channel)#Error
# a11="This is {1} and his channel is {}..".format(name,channel)#Error
# a12="This is {} and his channel is {0}..".format(name,channel)#Error
# a13="This is {} and his channel is {1}..".format(name,channel)#Error
print(a)
print(a1)
print(a2)
print(a3)
print(a4)
print(a8) 
print(a9) 
