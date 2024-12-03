# 5 :55
class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod#class method aapke program me class ko available karra dete hai instance ke bajaye.
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Employee()
# e1.show() #Error
e1.name="Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()

print(Employee.company)