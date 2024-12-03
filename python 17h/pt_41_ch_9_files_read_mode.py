# Use Open function to read the content of the file:
"NOTE :write and append mode can create a file but read does not.."
"Opening a file in read mode:"
f= open("sample.txt","r")#If you don't specify the mode than python compiler will take by default mode as an r..
# f= open("sample.txt")#If you don't specify the mode than python compiler will take by default mode as an r..
# data =f.read()
data =f.read(5)#yeah sirf 5 character ko hi read karega..
print(data)
f.close()