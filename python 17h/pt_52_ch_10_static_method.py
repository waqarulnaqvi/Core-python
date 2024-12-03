"""
staic method:
Sometimes we need a function that doesn't use the self parameter we can define a static method like this:

    @staticmethod#static method decorator..->decorator to mark greet as a static method..
    def greet():
        print("Good Morning,sir!") 
"""        
class Employee:
    company="Google"
    salary =12
    def getSalary(self,signature):#you have to pass self because self automatically pass in python function..
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    # def greet(delta):
    #     print("Good Morning,sir!")  

    # def greet(self):
    #     print("Good Morning,sir!")   
    
    @staticmethod#static method decorator..->decorator to mark greet as a static method..
    # decorator ek special tarha ka function hota jo function ko modify karta hai..
    def greet():
        print("Good Morning,sir!")   

harry =Employee()
harry.greet()
# harry.salary=10000
harry.getSalary("Thanks!")#"self" ki help se aap is harry object ke saare instance attributes or saare class attribute ko print kar sakte hai..
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
