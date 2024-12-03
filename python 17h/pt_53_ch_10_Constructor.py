"""
__init__() Constructor:
__init__() is a special method which is first run as soon as the object is created..
__init__() method is also known as constructor..

#we call it name as an constructor because it initialize the object..

It takes self argument and can also take further arguments..
Example given below:
"""  
class Employee:
    company="Google"
    salary =12
    def __init__(self,name,salary,subunit) :
        # we will use same name in both of the side in most the cases..
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")


    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    # def greet(delta):
    #     print("Good Morning,sir!")  

    # def greet(self):
    #     print("Good Morning,sir!")   
    
    @staticmethod
    def greet():
        print("Good Morning,sir!")

    def getDetails(self):
        print(f"\nThe name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")       
        print(f"The subunit of the employee is {self.subunit}\n")       

harry =Employee("Waqarul",100,"YouTube")
# greet()#Error..
# harry.greet()
# harry.salary=10000
# harry.getSalary("Thanks!")
harry.getDetails()
# print(harry.subunit)#Run..
harry.subunit="Facebook"#Run..
# print(harry.subunit)#Run..
harry.getDetails()

