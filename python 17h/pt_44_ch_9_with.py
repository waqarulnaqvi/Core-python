# with is called as an context manager..
with open('another.txt',"r") as f:
    a= f.read()
with open('another.txt','w') as f:
    a= f.write("I am the alpha male!")
print(a)    
"""With Statement:
The best way to open and close the file automatically is the with statement..
     with open("this.text") as f:
        f.read() ->Dont need to write f.close() as it is done automatically..
"""