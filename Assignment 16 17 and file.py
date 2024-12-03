# [0:27 pm, 16/06/2023] Azan2: Assignment on files
# Write a Python program to read an entire text file.
# Write a Python program to read first n lines of a file.
# Write a Python program to append text to a file and display the text.
# Write a Python program to read last n lines of a file.
# Write a Python program to read a file line by line and store it into a list.
# Write a Python program to count the number of lines in a text file.
# [0:28 pm, 16/06/2023] Azan2: Assignment 16

# Write a Python program to create a set.
# SET={1,2,4,5}
# print(type(SET))
# Write a Python program to iterate over sets.

# Write a Python program to add member(s) in a set.
# SET={1,2,3,4}
# SET.add(23)
# print(SET)

# Write a Python program to remove item(s) from set
# SET={1,2,3,4}
# print(SET)
# SET.remove(4)
# print(SET)


# Write a Python program to remove an item from a set if it is present in the set.
# SET={1,2,3,4}
# SET.discard(22)
# print(SET)


# Write a Python program to create an intersection of sets.
# SET={1,2,3,4}
# SET2={3,4,5,7,}
# print(SET.intersection(SET2))

# Write a Python program to create a union of sets. rite a Python program to create set difference.
# 14 8
# SET={1,2,3,4,5}
# SET1={4,6,7}
# print(SET.union(SET1))

# Write a Python program to create a symmetric difference.


# Write a Python program to check if a set is a subset of another set.
# SET={1,2,3,4,5}
# SET1={4,5}
# print(SET1.issubset(SET))

# Write a Python program to clear a set.
# SET={1,2,3,4,5}
# Write a Python program to find maximum and the minimum value in a set.
# SET={1,233,31,44,5,6}
# max=-1212121
# min=1212121
# for i in SET:
#     if(max<i):
#         max=i
#     if(min>i):
#         min=i
# print(f"MAXIMUM VALUE IS {max} ,MINIMUM VALUE IS {min}")

 # Assignment 17
# Write a Python program to find the length of a set.
# SET={1,2,4,5,53}
# print(len(SET))

# Write a Python program to check if a given value is present in a set or not.
# SET={1,2,4,5,53}
# if 1 in SET:
#     print("Yes it is in!!")
# else:
#     print("No it is not in!!")

# Write a Python program to check if two given sets have no elements in common
# SET={1,2,4,5,53}
# SET1={23,432}
# print(SET.isdisjoint(SET1))

# Write a Python program to check if a given set is superset of itself and superset of another given set

# Write a Python program to find the elements in a given set that are not in another set.

# Write a Python program to check a given set has no elements in common with other given set.

# Write a Python program to remove the intersection of a 2nd set from the 1st set.
# SET={1,22,4,5,53}
# SET2={25,22,42,533,53}
# Inter=SET.intersection(SET2)
# for i in Inter:
#     SET2.remove(i)
#
# print(SET2)

# f= open('myfile.txt','r')
# #read 'r' mode is a default mode.
# # print(f)
# txt=f.read()
# print(txt)
# f.close()
#print(f.read())# Error because file is close.

"""Write mode 'w mode' .In this mode file will created by compiler."""
"""If file is does not exists it this mode create a file and add the content .if file is exists this mode re-write the content inside the file."""
# f=open('myfile2.txt','w')
# f=open('pythonfile.py','w')
# txt=f.write('print("Helloorld")')
# f.close()

# f=open('myfile.txt','rb')#open the file in the binary form.
# print(f.read())
# when we want to open a exe or pdf file etc.

#append mode:
"""Append mode 'a mode' .In this mode file will created by compiler."""
"""If file is does not exists in this mode create a file and add the content. If file is exists this mode add the content of the file again and again whenever we run the code."""
# f=open('myfl.txt','a')
# txt=f.write('print("Hello world")')
# print(f.read())
# f.close()
#
# with open ('myfile.txt','a') as f:
#     f.write("jeeererer")
# # 2 42

# Assignment on files
# Q1)Write a Python program to read an entire text file.
# with open("text.txt","r") as f:
#     txt=f.read()
#     print(txt)


# # Q2)Write a Python program to read first n lines of a file.
# with open("text.txt","r") as f:
#     txt=f.read(int(input("Enter the value of n:")))
#     print(txt)
#
# # 12 24
#
# # Q3)Write a Python program to append text to a file and display the text.
# f=open('text.txt',"a")
# txt="BBD Examination process is inhuman!!\n"
# f.write(txt)
# print(f"Appended text is : {txt}")
# f.close()
# 12 48
#  1 2

# Q4) Write a Python program to read last n lines of a file.
# f=open('text.txt',"r")
# lines=f.readlines()[ -int(input("Enter n :")): ]
# for line in lines:
#     print(line,end="")
# f.close()

# Q5) Write a Python program to read a file line by line and store it into a list.
# list=[]
# f=open('text.txt',"r")
# lines=f.readlines()
# for line in lines:
#     print(line,end="")
#     list.append(line)
# print(list)
# f.close()

# Q6) Write a Python program to count the number of lines in a text file.
with open("text.txt") as f:
    lines=f.readlines()
    print(len(lines))