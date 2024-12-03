"""Problem:1
class C2dVec:
    # @staticmethod#Error.. #you can not make constructor as an static method..
    def __init__(self,i,j):
        self.icap =i
        self.jcap =j
        
    def __str__(self):
        return f"{self.icap}i +{self.jcap}j" 

class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i +{self.jcap}j +{self.kcap}k"         

v2d= C2dVec(1,3)
v3d= C3dVec(1,3,7)
print(v2d)  #it run properly because of "__str__(self)" method.. 
print(v3d)  #it run properly because of "__str__(self)" method.. 
"""

"""Problem:2
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bhaw bhaw!")
d=Dog()
print(d.bark()) #it print bhaw bhaw! and return None in output..
"""

"""Problem:3
# salaryAfterIncrement = salary * Increment
class Employee:
    # company="Bharat Gas"
    salary=1000
    # salarybonus=600
    increment=1.5
    # totalSalary=6100

    # getter decorator:
    @property # also called as a getter method..
    def salaryAfterIncrement(self):#yeah internally function ko run karega or value generate karega or fir ese return kar dega jaise ki yeah ek property ho..
        return self.salary*self.increment

    # setter decorator:
    @salaryAfterIncrement.setter # also called as a setter method..
    def salaryAfterIncrement(self,sai):
        self.increment =sai/self.salary


e=Employee()
print(e.salaryAfterIncrement)
print(e.increment,"times")

e.salaryAfterIncrement =3000
print(e.increment,"times")
print(e.salaryAfterIncrement)

e.salaryAfterIncrement =10
print(e.increment,"times")
print(e.salaryAfterIncrement)
"""

"""Problem:4
# multiplication of complex number:
# (a+bi)(c+di)=(ac-bd)+(ad+bc)i

class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
   
    def __add__(self,c):
        return Complex(self.real+ c.real,self.imaginary +c.imaginary)
    
    def __mul__(self,c):
        mulReal =self.real*c.real-self.imaginary*c.imaginary
        mulImg =self.real*c.imaginary+self.imaginary*c.real
        return Complex(mulReal,mulImg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"  
        else:
            return f"{self.real} + {self.imaginary}i"      
          

c1 =Complex(1,-4)
c2 =Complex(331,-37)
c3 =Complex(3,2)
c4 =Complex(1,7)
print(c1+c2)
print(c3+c4)
print(c1+c2+c3+c4)

print(c1*c2)
print(c3*c4)
print(c1*c2*c3*c4)
"""

'''Problem:5
class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=""
        index=0
        # for i in range(len(self.vec)):
        for i in self.vec:
           str1 +=f" {i}a{index} +"
           index+=1  
        return str1 [:-1]    

    def __add__(self,vec2):
        newlist =[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum +=self.vec[i] * vec2.vec[i]
        return sum

v1=Vector([1,4,6,6])
v2=Vector([1,6,9,8])
print(v1+v2)#it will be a vector quantity not a scalar quantity..
print(v1*v2)#it will be a scalar quantity not a vector quantity..

"""Tips:
a=[2,4]
b=[3,4]
print(a+b)#Output:[2, 4, 3, 4] "+" Operator will append the list.. 
"""
'''

"""Problem:6
class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=""
        index=0
        # for i in range(len(self.vec)):
        for i in self.vec:
         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"    
v1=Vector([1,4,6])
v2=Vector([1,6,9])
print(v1)
print(v2)
"""

"""Problem:7"""
class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=""
        index=0
        # for i in range(len(self.vec)):
        for i in self.vec:
           str1 +=f" {i}a{index} +"
           index+=1  
        return str1 [:-1]    

    def __add__(self,vec2):
        newlist =[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum +=self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)    

v1=Vector([1,4,7,8,])
v2=Vector([1,6,9,8,7])
print(len(v1))
print(len(v2))
"""Method:1"""
if (v1.__len__()!=v2.__len__()):
    print("Addition and multiplication operation can only be performed in the same length vector..") 
else:
    print(v1+v2)#it will be a vector quantity not a scalar quantity..
    print(v1*v2)#it will be a scalar quantity not a vector quantity..  


"""Method:2
if (v1.vec.__len__()!=v2.vec.__len__()):
    print("Addition and multiplication operation can only be performed in the same length vector..") 
else:
    print(v1+v2)#it will be a vector quantity not a scalar quantity..
    print(v1*v2)#it will be a scalar quantity not a vector quantity..        
"""