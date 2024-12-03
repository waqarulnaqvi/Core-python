class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is python")
e=Employee("rohan Das",343)
e.showDetails()
d=Programmer("rohan Das",343)
d.showDetails()
d.showlanguage()
