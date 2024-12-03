#String can be write as both ' ' single quote and " " double quote
str="He said ,'I am a bad boy' "
str1='He said ,"I used to be a good boy"'
str2="""'Multi
line 
String'"""
str3='''"Multi 
LIne 
String"'''
print(str)
# print(str[44])#IndexError: string index out of range
print(str[-5])#Run..
print(str[24])
print(str[25])
# print(str[26])#IndexError: string index out of range
print(str1)
print(str2)
print(str3)

# for loop
print("I am for loop of str")
for i in str:#it is like a Enhanced for loop
    print(i)#
    
    # for loop
print("I am for loop of str1")
for i in str1:#it is like a Enhanced for loop
    print(i)

    # for loop
print("I am for loop of str2")
for i in str2:#it is like a Enhanced for loop
    print(i)

    # for loop
print("I am for loop of str3")
for i in str3:#it is like a Enhanced for loop
    print(i)