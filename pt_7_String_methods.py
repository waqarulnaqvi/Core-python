# String are also immutable in python
# String methods aapki existing string pe operate karte hai or new string return me de dete hai..
a="!! !!Ha rry!!!"
print(len(a))

print(a.rstrip("!"))#same #it remove the ! only from the end not from the beginning!!
print(a.rstrip("@"))#not remove the !
print(a.rstrip("!!!~!!"))#same #it remove the ! only from the end not from the beginning!!

print(a.upper())

print(a.lower())

print(a.replace("Har","karry"))
print(a.replace("Hari","karry")) #does not do anything!!

#split(): The split() method splits the given string at the specified instance and returns the separated strings as list items.
# capitalize(): The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
print(a.split(" "))
print(a.split("!"))

blogheading ="introdUction to jS"
print(len(blogheading.capitalize()))

print(blogheading.center(30))
print(len(blogheading.center(30)))

print(blogheading.center(40))
print(len(blogheading.center(40)))

print(blogheading.center(50))
print(len(blogheading.center(50)))

print(a.count("Harry"))
print(a.count("Ha rry"))
print(a.count("!"))

# print(a.endswith("!"))
# print(a.endswith("7"))
# print(a.endswith("Ha",0,7))
#
# print(a.find("Ha"))
# print(a.find(" "))
# print(a.find("chutiya"))
# print(a.find("zamanboni"))
# print(a.find("zamanboni"))
# #find method index method ke similar hota hai but find method me value na milne pe -1 return hota hai but index method pe value na milne pe error aata hai..
# k="k's is "
# print(k.find("is"))
# print(k.find("ish"))
# print(k.index("is"))
# # print(k.index("ish")) #ValueError: substring not found
#
# # isalnum(): The isalnum() method returns True only if the entire string only consists of A-Z,a-z,0-9.If any other characters or punctuations are present,then it returns False.
# k="he#lo"
# k1="787"
# k2="AQW"
# k3=" "
# k4="$%$#%$^%^&**&()!@~"
# print(k.isalnum())
# print(k1.isalnum())
# print(k2.isalnum())
# print(k3.isalnum())
# print(k4.isalnum(),"\n\n")
#
# # alphanumeric() me number bhi aate hai or sirf alpha() me numbers ni aate hai..
# k="hel3o"
# k1="787"
# k2="AQW"
# k3=" "
# k4="$%$#%$^%^&**&()!@~"
# print(k.isalpha())
# print(k1.isalpha())
# print(k2.isalpha())
# print(k3.isalpha())
# print(k4.isalpha(),"\n\n")
#
#
# k="ERE"
# k1="efdf"
# k2="232"
#
# print(k.islower())
# print(k.isdecimal())
# print(k.isupper())
# print(k.isdigit(),"\n\n\n")
#
# print(k1.islower())
# print(k1.isdecimal())
# print(k1.isupper())
# print(k1.isdigit(),"\n\n\n")
#
# print(k2.islower())
# print(k2.isdecimal())
# print(k2.isupper())
# print(k2.isdigit(),"\n\n\n")
#
# k="\n"
# k1="rtrter ##$#DGGDG\nrtrtr\tERer"
# k2="$%$%$%gfsdgsdtwrtw W2323RW\\\"\'R"
# k3="$%$%$%gfsdgsdtwrtwW 2323RW\\\"\'\t\tR"
# print(k.isprintable())
# print(k1.isprintable())
# print(k2.isprintable())
# print(k3.isprintable(),"\n\n\n")
#
# k="\n"
# k1=" "
# k2="\t"
# k3="$%$%$%gfsdgsdtwrtwW 2323RW\\\"\'\t\tR"
# print(k.isspace())
# print(k1.isspace())
# print(k2.isspace())
# print(k3.isspace(),"\n\n\n")
#
# # istitle() : The istitle() returns True only if the first letter of each word of the string is capitalized,else it returns False..
# k="\n"
# k1="Jtttt Rdfdf\tR#\\\"\'"
# k2="EER qERgfsdgsdtwrtw wEWEWEW23 "
# k3="E$%$%$%gf Esdgsdtwrtw W2323R\\\"\'\t\tRer"
# print(k.istitle())
# print(k1.istitle())
# print(k2.istitle())
# print(k3.istitle(),"\n\n\n")
#
# print(k.startswith("\n"))
# print(k.startswith(""))
# print(k1.startswith("Jttt"))
# print(k1.startswith("Jttt45"))
#
# print(k.swapcase())
# print(k1.swapcase())
# print(k2.swapcase())
# print(k3.swapcase())
#
# print(k.title())
# print(k1.title())
# print(k2.title())
# print(k3.title())