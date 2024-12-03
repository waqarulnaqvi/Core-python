"""Problem:1
''' (my logic)
try:
    with open('another.txt',"r") as f:
       a= f.read()
       print(a)

    f= open("sample.txt","r")
    data =f.read(5)
    print(data)
    f.close()   

    with open('king.txt',"r") as f:
       a= f.read()
       print(a)

except Exception as e:
    print(e)
'''

''' (cwh logic)'''
class read:
    def __init__(self,filename):
        self.filename=filename

    def readfile(self):
        try:
            with open(self.filename,"r") as f:
                print(f.read(21))
        except FileNotFoundError:
            print(f"File {self.filename} is not found..")

re=read('another.txt')
re.readfile()
rea=read('king.txt')
rea.readfile()
reaa=read("sample.txt")
reaa.readfile()
"""

"""Problem:2
# for i in range(1,8,2):
#     print (i)
# print()   
list1=[3,23,3.43,False,"Waqarul","l","34ewrsw"]

for index,item in enumerate(list1):
    # if(index%2!=0):
    #     print(index,item)

    if(index==0):
        continue
    if(index%2==0):
        print(index,item)
"""



"""Problem:3
'''(my logic)
a =[2,3,44,55,64,22,11,3,5,7,9,223,22]
k=int(input("Enter a number:"))
print(f"Multiple of {k} found in list is:")
# List_Comprehensions:
b=[i for i in a if i%k==0]
print(b)   
'''

'''(cwh logic)'''
k=int(input("Enter a number:"))
# List_Comprehensions:
table=[k*i for i in range(1,11) ]
print(table)
"""

"""Problem:4
try:
    b=int(input("Enter a number:"))
    a=50000
    print(f"{a}/{b}=={a/b}")

except ZeroDivisionError as e:
    print(e)   

# except ValueError as e:
#     print(e)

except Exception as e:
    print(e)
"""

"""Problem:5"""
'''(my logic)
a =[2,3,44,55,64,22,11,3,5,7,9,223,22]
k=int(input("Enter a number:"))
# print(f"Multiple of {k} found in list is:")
b=[i for i in a if i%k==0]
# print(b) 
  
with open('Tables.txt','a') as f:
    f.write(f"Multiple of {k} found in list is: \n {str(b)} \n\n")
    # l=f.read()#it only used in read mode..
    
with open("Tables.txt") as f:
    print(f.read())
'''

'''(cwh logic)'''
k=int(input("Enter a number:"))
# List_Comprehensions:
b=[k*i for i in range(1,11) ]
# print(table)

with open('Tables.txt','a') as f:
    f.write(f"Multiple of {k} is: \n {str(b)} \n\n")
    # l=f.read()#it only used in read mode..
    
with open("Tables.txt") as f:
    print(f.read())