class Employeee:
    salary=100
    company ="Google"#class attributes..

# print(harry=Employeee())#Error..
harry=Employeee()#rajini and harry is a instance of a class..
rajini=Employeee()
# Creating instance attributes salary for both the objects:
# harry.salary=300
# rajini.salary=400
"""Instance Attributes:
An attribute that belongs to the instance(object).Assuming the class from the previous example:

harry.name="Harry
rajini.salary=400  =>Adding instance attributes..
Note: Instance attributes take preference over class attributes during assignment & retrival..

harry attributes ->1)Is attribute present in object?(first preference)
                   2)Is attribute present in class?(second preference)
"""
print(harry.company)
print(rajini.company)
Employeee.company="Youtube"#class attribute so changing with class name..
print(harry.company)
print(harry.salary)
print(rajini.company)
print(rajini.salary)
