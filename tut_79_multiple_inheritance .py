class Employee:
    def __init__(self,name):
        self.name=name

    def show_details(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show_details(self):
        print(f"The dance is {self.dance}")


# class Employee_Dancer(Employee,Dancer,Dancer): #Error
class Employee_Dancer(Employee,Dancer):
    def __init__(self,name,cap,dance):
        self.name=name
        self.dance=dance
        self.cap=cap

# 4 52 - 5 32
e=Employee("shiv")
print(Employee.mro())
# print(e.mro())#Error

d=Dancer("khuchipuri")
print(Dancer.mro())

o=Employee_Dancer("Shivani","Kathak","toopa")
print(Employee_Dancer.mro())
# print(o.mro()) #AttributeError: 'Employee_Dancer' object has no attribute 'mro'
print(o.name)
o.show_details()