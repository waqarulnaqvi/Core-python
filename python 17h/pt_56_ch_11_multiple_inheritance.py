"""Multiple Inheritance:"""
class Employee:#base,parent class..
    company="Google"
    ecode =120

    # def showDetails(self):
    #     print("This is an employee!")

class Freelancer:#base,parent class..
    company="Fiverr"
    level =0

    def upgradeLevel(self):
        self.level=self.level +1

class Programmer(Freelancer,Employee):#child,derived class..
    #Freelancer class humne pehle likhi hai isliye iski property or methods ko priority di jaayegi..
    # jo bhi class hum pehle likhte uske property or methods ko priority di jaati hai..
    name="Naqvi"
    # language="Python"
    # company="Youtube"

    # def getLanguage(self):
    #     print(f"The language is {self.language}")

    # def showDetails(self):
    #     print("This is an Programmer!")    

e =Employee()
p=Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)
