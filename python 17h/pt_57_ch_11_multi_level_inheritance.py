"""Multi level Inheritance:"""
class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company="Google"
     
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        # return super().takeBreath()
        print("I am an Employee so I am luckily breathing..")


class Programmer(Employee):
    name="Naqvi"
    company="Youtube"

    def getSalary(self):
        print(f"No salary to programmers..")

    def takeBreath(self):
        # return super().takeBreath()
        print("I am an Programmer so I am breathing ++..")


p=Person()
p.takeBreath()
# print(p.company)#p(person) does not have any company,so it throws an error..
print(p.country)

e=Employee()
e.takeBreath()
print(e.company)
print(e.country)

pr=Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
