"""
super() method:
super method is used to access the methods of  a super class in the derived class..

super().__init__()
                 |
                 > calls constructor of the base class..
"""
"""Multi level Inheritance:"""
class Person:
    country = "India"

    def __init__(self):
        print("Initailizing Person...\n")

    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company="Google"

    def __init__(self):
        super().__init__()
        print("Initailizing Employee..\n")
     
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    name="Naqvi"
    company="Youtube"

    def __init__(self):
        super().__init__()
        print("Initailizing Programmer..\n")

    def getSalary(self):
        print(f"No salary to programmers..")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am breathing ++..")


# p=Person()
# p.takeBreath()
# print(p.company)#p(person) does not have any company,so it throws an error..
# print(p.country)

# e=Employee()
# e.takeBreath()
# print(e.company)
# print(e.country)

pr=Programmer()
pr.takeBreath()
# print(pr.company)
# print(pr.country)
