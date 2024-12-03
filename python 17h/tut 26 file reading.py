f= open("tut 26.txt","rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content=f.read() #f.read() will blank the file pointer for the next time.
# for line in content:
#     print(line)
# for line in f: #f.read() will blank the file pointer for the next time so you can use this.
#     print(line, end="")
# print(content)
# content=f.read(334535)
# print("1",content) #if you print read function default means full txt then if you print content twice complier will not print content again.
#
# content=f.read(3)
# print("2",content)

f.close()#All the tide up file resources will be free.
#this closes all the file resources and it is a good practise.