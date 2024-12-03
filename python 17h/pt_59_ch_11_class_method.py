class Employee:
    company="Camel"
    salary=1000
    location="Delhi"


    # def changeSalary(self, sal):#it created the instance attribute.. it does not change the class attribute..
    #     self.salary=sal 
   
    # def changeSalary(self, sal):# it changes the class attribute..
    #     self.__class__.salary=sal #dunder class to change class attributes method..

    """class metods:
    A class method is a method which is bound to the class and not the object of the class..
    @classmethod decorator is used to create a class method..
    
    Syntax to create a class method:

    @classmethod
    def(cls,p1,p2):
        ...
    """
    @classmethod
    def changeSalary(cls, sal):# it changes the class attribute..
        cls.salary=sal 

e=Employee()
print(e.salary)   
e.changeSalary(455)
print(e.salary)
print(Employee.salary)