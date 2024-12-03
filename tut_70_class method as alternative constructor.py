class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Example of class methods as an alternative constructor
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e=Employee("WAQArul",12000)
print(e.name)
print(e.salary,end="\n\n")
# 7 57
# 8 20
# 2 h 37 min

string="Harry-12000"
e1=Employee(string.split("-")[0],string.split("-")[1])
print(e1.name)
print(e1.salary)
print()

e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary+123)

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age


    @classmethod
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))

p=Person(12,"fdfsfsf")
print(p.name)
print(p.age)
print()

p=Person.from_string("JohanDe,34")
print(p.name)
print(p.age)