"""Problem:1
f = open("poem.txt")
t =f.read()
if 'Twinkle' in t:
    print("Twinkle is present")
else:
    print('Twinkle is not present')
f.close()        
"""

"""Problem:2
def game():
    return 42

score=game()
with open("hiscore.txt") as f:
    hiscorestr=f.read()
    
if hiscorestr=='':
    with open("hiscore.txt",'w') as f:
        f.write(str(score))   

elif int(hiscorestr)<score :
    with open("hiscore.txt",'w') as f:
        f.write(str(score))
"""

"""Problem:3
for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}.txt",'w') as f:
        for j in range(1,11):
           f.write(f"{i} X {j} = {i*j}")
           if j!=10:
            f.write('\n')
    break   
"""

"""Problem:4
with open("sample.txt") as f:
    content =f.read()

content= content.replace("chutiya","@##$#%#$@#$")

with open("sample.txt","w") as f:
    f.write(content)
"""

"""Problem:5
words=["donkey","kaddu","mote","chutiya"]
with open("sample.txt") as f:
    content =f.read()
    print (content+"\n")


for word in words:
    content= content.replace(word,"@##$@#$")

    with open("sample.txt","w") as f:
      f.write(content)
print (content)
"""

"""Problem:6
with open ("log.txt") as f:
    # content= f.read().upper()
    content= f.read()
k="PyTHON"
# if k.lower() in content:
if k.casefold() in content:
    print("Yes python is present")   
else:
    print("No python is not present")    
"""    

"""Problem:7
content=True
i=0
k1=True
with open ("log.txt") as f: 
    while content:   
        i+=1 
        content= f.readline()   
        k="PyTHON"
        if k.casefold() in content:
           k1=False
           print("Yes python is present") 
           print(f"line number:{i}")  
           print(content)
           
           
    if k1 :
        print("No python is not present")    
"""       

"""Problem:8
with open("this.txt") as f:
    content=f.read()

with open("copy.txt",'w') as f:
    f.write(content)
"""

"""Problem:9
file1="copy.txt"
file2="this.txt"
# file2="log.txt"

with open(file1) as f:
    f1=f.read()

with open(file2) as f:
    f2=f.read()

if f1==f2:
    print("files are identical")
else:
    print("files are not identical")   
"""    

"""Problem:10
filename="copy.txt"
with open(filename,"w") as f:
    f.write("")
"""  

"""Problem:11"""
import os
oldname='copy2.txt'
newname="renamed_by_python.txt"
with open(oldname) as f:
    content=f.read()

with open(newname,'w') as f:
    f.write(content)

os.remove(oldname)    