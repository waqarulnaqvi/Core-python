class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

    def __str__(self):
        return  (f"The name of the employee is {self.name} str")
    # repr ek method hai jo represent karta hai object ke us tareeke ko jisse isse recreate kiya jaata hai.

    def __repr__(self):
        return  (f"The name of the employee is ('{self.name}') repr")

    # def __call__(self):
    #     print("Hey I am good")

    def __call__(self):
       return "Employee object cannot be collable"

# e=Employee("Harry")