# Use Open function to read the content of the file:
"NOTE :write and append mode can create a file but read does not.."
"Opening a file in read mode:"
# f= open("sample.txt","r")#If you don't specify the mode than python compiler will take by default mode as an r..
f= open("sample.txt")#If you don't specify the mode than python compiler will take by default mode as an r..
# data =f.read()
# data =f.read(5)#yeah sirf 5 character ko hi read karega..
# readline() and readlines() mode in python:
data=f.readlines()
print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# data=f.readlines()
# print(data)
f.close()

"""
Modes of opening a file:
r -> open for reading.
w -> open for writing.
a -> open for appending.
+ -> open for updating..

'rb' will open for read in binary mode.(rb means read in binary mode).
'rt' will open for read in text mode.(rt means read in text mode).
'r' will open for read in text mode. #by default files open in text mode..

"""