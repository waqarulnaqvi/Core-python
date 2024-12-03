"""Single Inheritance:"""
class Employee:#base,parent class..
    company="Google"

    def showDetails(self):
        print("This is an employee!")

class Programmer(Employee):#child,derived class..
    language="Python"
    company="Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer!")    
e =Employee()
e.showDetails()
print(Employee.company)
print(e.company)
p=Programmer()
Programmer.showDetails(p)        
print(Programmer.company)
print(p.company)
