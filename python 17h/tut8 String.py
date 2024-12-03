"""# String is nothing but just a combination of character
mystr="Waqarul is a bad guy"#indexing in string in python starts from 0
print(len(mystr))
# String slicing
# Note:full string print karane ke liye ek element zada likhna hota hai string ki total length se "0" se count kar ke..
# print(mystr[0:110])
# print(mystr[0:221:2])
# print(mystr[3:221:2])
# print(mystr[0])
# print(mystr[0:])
# print(mystr[:9])
# print(mystr[9])
# print(mystr[:])
# print(mystr[::])#advance slicing /or also called as extended slice.
# print(mystr[::2])
print(mystr[-6:])
print(mystr[-6:-4])
print(mystr[: :-1])
print(mystr[: :-2])
# alpha numeric string means string with no spaces
# ex;
str="iAm not AgOOdguy"
print(str)
print(len(str))
# print(mystr.isalnum())
# print(str.isalnum())
# print(mystr.isalpha())
# print(str.isalpha())
# print(mystr.endswith("guy"))
# print(mystr.endswith("boy"))
# print(str.count("b"))
# print(str.count("a"))
print(str.capitalize())
print(str.find("is"))
print(str.find("a"))
print(str.upper())
print(str.lower())
print(str.replace("Am","are"))
#you can also search string function in python on google.."""

mystr="Waqarul is a good and bad guy";
# print(type(mystr))
# print(mystr)
# # print(mystr[4000])#String index out of range..
# print(mystr[-13])#it will run..
# print(mystr[0:5])#0 is included and 5 is excluded..
# # String is nothing just a combination of character..
# print(len(mystr[15]))#length will be 1
# print(len(mystr))#length will be 29
# print(mystr[0:29])#0 is included and 29 is excluded..
# print(mystr[0:2934])#it will run and print string length..
# print(mystr[0:2921:2])#it will skip one one character which is written in the end (2)..
# print(mystr[0::2])# khali jagha poori length le lega..
# print(mystr[:44:2])# khali jagha poori length =0 le lega..
# print(mystr[::])#print(mystr[poori length le lega :by default 0 length le lega: 1 le lega])
# print(mystr[::3])#print(mystr[: : 2 skip karega])
# print(mystr[::4])#print(mystr[: : 3 skip karega])
# isko advance or extended slice bolte hai..
# print(mystr[::-1])
print(mystr[23:-1:])
print(mystr[2::])
print(mystr[::-2])
print(mystr[::-3])

