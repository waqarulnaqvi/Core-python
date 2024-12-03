class Employee:
    company="Google"
    salary =12
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")#jis bhi object pe run kar rhe ho aap uska salary attribute yha pe aayega..

harry =Employee()
# harry.salary=10000
harry.getSalary()#"self" ki help se aap is harry object ke saare instance attributes or saare class attribute ko print kar sakte hai..
# Employee.getSalary(harry) 
# Internally yeah "harry.getSalary()" code  ese ->"Employee.getSalary(harry)" run hota hai.. 
"""
'self' parameters:
self refers to the instance of the class .It is automatically passed with a function call from an object..

harry.getSalary()->here self is harry
                |
                ->equivalent to Employee.getsalary(harry)

#variable ,attribute or property word interchageble use kiya jaata hai python me..
"""     