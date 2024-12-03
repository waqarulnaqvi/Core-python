#1 53
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

with open ('myfile.txt','a') as f:
    f.write("jeeererer")
# 2 42
