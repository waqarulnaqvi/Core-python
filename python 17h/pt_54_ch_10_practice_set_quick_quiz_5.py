# sometimes question is less in detail or mbqt is in the question so solve it according to your creativity..
"""Problem:1
class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is \
{self.name} and the product is {self.product}")


harry =Programmer("Harry","skype") 
Waqarul=Programmer("Waqarul","Dynmo")  
# print(Programmer("Waqarul","Dynmo")) #print address..
# print(harry = Programmer("Waqarul","Dynmo")) #Error..
harry.getInfo()
Programmer.getInfo(Waqarul)    
"""

"""Problem:2&4
import math
class Calculator:
    def __init__(self,num):
        self.number=num#Run properly..

    def operations(self):
        print()
        # print(f"The square of number is {self.number*self.number}")    
        print(f"The square of number is {self.number**(2)}")    
        # print(f"The cube of number is {self.number*self.number*self.number}")    
        print(f"The cube of number is {self.number**(3)}")    
        print(f"The square_root of number is {math.sqrt(self.number)}")   
        print(f"The square_root of number is {self.number**(0.5)}\n")   
    @staticmethod #Problem 4:
    def greet():
        print("Hello")
num=Calculator(12)    
# print(Calculator(12)) #print address..
num.operations()    
# num.number=9 
Calculator.operations(num)
num.number=9 
Calculator.operations(num)


num.greet()# Problem 4:
Calculator.greet()# Problem 4:

# harry.getSalary()->here self is harry
#                 |
#                 ->equivalent to Employee.getsalary(harry)
"""

"""Problem:3
class Sample:
    a="Naqvi"

obj=Sample()
obj.a='Vikky'#it set the new instance attributes but does not change the class attributes..
print(Sample.a)
print(obj.a)

Sample.a='Vikky'#it will change the class attributes..
print(Sample.a)
print(obj.a)
"""

"""Problem:5
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def book_a_ticket(self):
        if self.seats>0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("This train is full! kindly try in tatkaal..")   

    def status(number_of_seats):
        pass
    
    def getSatus(self):
        print("*************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are: {self.seats}")

    def fareInfo(hello):
        print(f"The price of the ticket is: Rs {hello.fare}")

    def cancelticket(self,seatNo):
        pass    


IdRailways=Train("\"Intercity Express :14015\"",90,2)
Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()
"""

"""Problem 6:"""
class Sample:
    def __init__(naqvi,name):
        naqvi.name=name#self is like a function parameter.. you can put any valid identifier here..but it is recommended you use "self" instead of any other name so that others programmer may not confuse.. if you are working on a big projects..

obj=Sample("Waqarul")
print(obj.name)

"""quick_quiz_5:Implement cancel ticket in problem 5 using lists
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def book_a_ticket(self):
        for i in range(self.seats.__len__()):
                 print(f"Your ticket has been booked! Your seat number is {self.seats[i]}")
                 self.seats.pop(i)
                 break
        else:
             print("This train is full! kindly try in tatkaal..")   

    def status(number_of_seats):
        pass
    
    def getSatus(self):
        print("*************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are: {self.seats.__len__()}")
        print(f"The seats number available in the train are: {self.seats}")

    def fareInfo(hello):
        print(f"The price of the ticket is: Rs {hello.fare}")

    def cancelticket(self,seatNo):
       i=0
       self.seats.insert(i,seatNo)  
       i=i+1
       print("Your seat has been cancel successfully!your money will be refunded with 24h..\n")


IdRailways=Train("\"Intercity Express :14015\"",90,[71,72])
Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()
inp=int(input("\nEnter your seat number which you want to cancel:"))
IdRailways.cancelticket(inp)
inp=int(input("\nEnter your seat number which you want to cancel:"))
IdRailways.cancelticket(inp)
inp=int(input("\nEnter your seat number which you want to cancel:"))
IdRailways.cancelticket(inp)


Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()
inp=int(input("\nEnter your seat number which you want to cancel:"))
IdRailways.cancelticket(inp)

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()

Train.getSatus(IdRailways)
Train.fareInfo(IdRailways)
IdRailways.book_a_ticket()
"""
