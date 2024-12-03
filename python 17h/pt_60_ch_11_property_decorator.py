class Employee:
    company="Bharat Gas"
    salary=5600
    salarybonus=600
    # totalSalary=6100

    # getter decorator:
    @property # also called as a getter method..
    def totalSalary(self):#yeah internally function ko run karega or value generate karega or fir ese return kar dega jaise ki yeah ek property ho..
        return self.salary +self.salarybonus

    # setter decorator:
    @totalSalary.setter # also called as a setter method..
    def totalSalary(self,val):
        self.salarybonus =val -self.salary


e=Employee()
print(e.totalSalary)
e.totalSalary =5800 #yeah likhne se "totalSalary ka setter" wala method run ho jaata hai automatically.."totalSalary ke setter" method ki wajhe se "salary bonus" bhi automatically change ho jaayega..
print(e.salary)
print(e.salarybonus)
print(e.totalSalary)
