# Question 1:
# str="hello"
# print(len(str))

# Question:2
# class find_freq:
#     def num_of_character(self,str):
#         self.dict={}
#         for i in str:
#             if i in self.dict:
#                 # print("It's i",i)
#                 self.dict[i]+=1
#                 # print("It's self.dict[i]",self.dict.get(i))
#             else:
#                 self.dict[i]=1
#         return self.dict
#
# inp=input("Enter a String:").lower()
# a=find_freq()
# print(a.num_of_character(inp))

# Question:3
# string="The weather is not too poor today"
# not_index=string.find('not')
# # print(poor_index)
# poor_index=string.find('poor')
# # print(not_index)
# newstr=""
# if not_index!=-1 and poor_index!=-1 and not_index<poor_index:
#     print(11)
#     newstr=string.replace(string[not_index:poor_index+4],"good")
#
# print(newstr)

# Question:4
# string="This is a String"
# for i,v in enumerate(string):
#     if i%2!=0:
#         print(v, end="")
#
# print()
#
# for i in range(1,len(string),2):
#     print(string[i],end="")




# Question:5(Change the case of every letter and word)
# def low_to_upp_and_upp_to_low(input):
#     print("Original String :", input)
#     print("New String :", end="")
#     for i in input:
#         # if i == i.lower():
#         if i.islower():
#             print(i.upper(), end="")
#         else:
#             print(i.lower(), end="")
# input="I Love Programming."
# low_to_upp_and_upp_to_low(input)


# Question:6
# def capitalixe_vowel(word):
#     vowels=['a','e','i','o','u']
#     capitalixe_word=""
#
#     for char in word:
#         if char.lower() in vowels:
#             char=char.upper()
#         capitalixe_word+=char
#     return capitalixe_word
#
# inp="a fdsfe i eereo urf"
# print(capitalixe_vowel(inp))

# Question:7
# string="This is a String"
# ucase=""
# lcase=""
# for i in string:
#     if i.islower():
#         lcase+=i
#     elif i.isupper():
#         ucase+=i
#
# print(f"lower case in a string is \"{lcase}\" and it's count is {len(lcase)}\nupper case in a string is \"{ucase}\" and it's count is {len(ucase)}")


# Question:8
# Split() function split the string into the list/array of substring.
# def func(str):
#     s=str.split()[::-1]
#     # print(type(s))
#     print(" ".join(s))
#     # return str[::-1]#it reverse the string.
# inp=input("Enter a string:")
# func(inp)

# Question:9
# inp=input("Enter a binary number:")
# dict={}
# len=1
# for i in inp:
#     if "1" in dict:
#         dict[i] += 2 ** len
#         len += 1
#     else:dict[i]=1
# print("{} decimal equivalent is :{}".format(inp,dict["1"]))
# print(dict)


