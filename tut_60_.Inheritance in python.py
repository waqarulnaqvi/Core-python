class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):
    @staticmethod
    def showlanguage():
        print("The default language is python")
e=Employee("rohan Das",343)
e.showDetails()  #calling method with a instance or object.
d=Programmer("prakash Das",3243)
d.showDetails()  #calling method with a instance or object.
# Programmer.showDetails() #it can not be call with a class name because it is non-static method.
Programmer.showlanguage() #it can be call with a class name because it is static method.
d.showlanguage()  #calling method with a instance or object.
