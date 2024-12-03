"""Problem:1
pip freeze->Enter(to know the details of all the packages which is installed in Python environment/Python virtual environment)
pip freeze > requirements.txt ->Enter(pip freeze ke saare content ko uthake requirement.txt me daal do)..
pip freeze > virtual_requirement.txt ->Enter(pip freeze ke saare content ko uthake virtual_requirement.txt me daal do)..
# "requirments.txt" file humare virtual environment ke saare modules/packages ka wrap hai..
(Answer) pip install -r .\"requirements returns.txt" ->Enter (to install all the module/packages present in the requirements returns.txt)
"""

"""Problem:2
name=input("Enter a name:")
marks=int(input("Enter a marks:"))
phone_no=int(input("Enter a phone number:"))
# print("The name of the student is {2}, his marks are {} and phone number is {0}".format(phone_no,marks,name))#Error..
print("\"The name of the student is {2}, his marks are {1} and phone number is {0}\"".format(phone_no,marks,name))
template="\"The name of the student is {2}, his marks are {1} and phone number is {0}\""
output=template.format(phone_no,marks,name)
print(output)
"""

"""Problem:3
'''(my logic)
# g5=lambda  num*i:for i in range(1,11)#Error..
list=["7","14","21","28","35","42","49","56","63","70"]
print(list)
vertical_table= "\n".join(list)
print(vertical_table)
'''

'''(cwh logic)'''
num=int(input("Enter a number:"))
list=[str(i*num) for i in range(1,11)]
print(list)
vertical_table= "\n".join(list)
print(vertical_table)
"""

"""Problem:4
def divisible_by_5(num):
    if num%5==0:
        return True
    else:
        return False

g10=lambda num:num %5==0

l=[15,25,3,45,5,6,75,85,89,98]
print(list(filter(divisible_by_5,l)))
print(list(filter(g10,l)))
print(list(filter(lambda num:num %5==0,l)))
"""

"""Problem:5
from functools import reduce

def max1(a,b):
    if(a>b):
        return a
    else:
        return b
    
a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
c=int(input("Enter a number 3:"))
d=int(input("Enter a number 4:"))
e=int(input("Enter a number 5:"))
l=[a,b,c,d,e]
print(l)
print(reduce(max1,l))
print(reduce(max,l))#here max is a inbuilt function which print the maximum value.. 
# print(max(a))#Error.. 
print(max(a,b))#max is a inbuilt function which print the maximum value.. 
# print(max(a,b,c))#Error..
# print(min(a))#Error..
print(min(a,c))#min is a inbuilt function which print the minimum value.. 
print(min(a,b,c))#min is a inbuilt function which print the minimum value.. 
print(min(a,b,c,d))#min is a inbuilt function which print the minimum value.. 
print(min(a,b,c,d,e))#min is a inbuilt function which print the minimum value.. 
"""

"""Problem:6
 Step 1:pip freeze
 Step 2:(pip freeze .\req2.txt) or (pip freeze req2.txt)
 Step 3: (.\req2.txt) or (req2.txt)
 Step 4: virtualenv codewithharry
 Step 5: (.\codewithharry\Scripts\activate.ps1) or (codewithharry\Scripts\activate.ps1) 
 Step 6:(pip install -r .\req2.txt) or (pip install -r req2.txt)    
"""

"""Proble:7
Step 1:Type on google "flask module"
Step 2:Click on Installation — Flask Documentation (2.2.x)
'''Navigation
Overview
Previous: Welcome to Flask
Next: Quickstart'''
Step 3:Click on "Next: Quickstart" guide 
Step 4:than copy the code and paste it..
Step 5:Copy the starter template and error message snipts from the bootstrap and paste it..
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
     <div class="alert alert-primary" role="alert">
  This is a primary alert—check it out!
</div>
<div class="alert alert-secondary" role="alert">
  This is a secondary alert—check it out!
</div>
<div class="alert alert-success" role="alert">
  This is a success alert—check it out!
</div>
<div class="alert alert-danger" role="alert">
  This is a danger alert—check it out!
</div>
<div class="alert alert-warning" role="alert">
  This is a warning alert—check it out!
</div>
<div class="alert alert-info" role="alert">
  This is a info alert—check it out!
</div>
<div class="alert alert-light" role="alert">
  This is a light alert—check it out!
</div>
<div class="alert alert-dark" role="alert">
  This is a dark alert—check it out!
</div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>'''

if __name__ =="__main__":
    app.run(debug=True)