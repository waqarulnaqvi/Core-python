# 6 9
# v1=1;v=77
# print(v1)
# print(v)

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i} i + {self.j} j + {self.k} k"

    def __add__(self, other):
        return Vector(self.i +other.i,self.j +other.j, self.k +other.k)

    def __sub__(self, other):
        return Vector(self.i -other.i,self.j -other.j, self.k -other.k)

    def __mul__(self, other):
        return Vector(self.i *other.i,self.j *other.j, self.k *other.k)


v1=Vector(3,5,6)
# print(v1)
v2=Vector(1,2,9)
# print(v2)
#
# print(v1+v2)
# print(v1+ Vector(3,2,5))
# print(v1*v2)
# print(v1-v2)
#
# print(type(v1))
# print(type(v1))
# print(type(v1+v2))
# 6 43
# 8 18
# 7 20
# 1h 35+35
# 2h 10 min
# Practice
class Point:
    # Python does not support constructor overloading.
    # def __init__(self,x):
    #     self.x=x

    def __init__(self,x,y):
        self.x=x
        self.y=y



    def  __add__(self, other):
        return Point(self.x+other.x ,self.y+other.y)

    def  __mul__(self, other):
        return Point(self.x *other.x,self.y*other.y)

    def  __repr__(self):
       return f"{self.x} and {self.y}"
    #
    def  __str__(self):
       return f"{self.x} and {self.y}"

    def __len__(self):
        l=0
        for c in str(self.x):
            l+=1
            # print(l)
        print(l)

    @classmethod
    def fromStr(cls,string):
        abc=str(string)
        return cls(int(abc[0]),int(abc[1]))

    @classmethod
    def integer(cls,integer):
        return cls(int(integer),int(integer))

# from  emp import *
# e=Employee("yellow")
# print(e.__call__())


p1=Point(821,2)
abc=82
p3=Point.fromStr(82)
p5=Point.integer(8)
print(p5,"Hello")
print(p1*p3)
p2=Point(19,2)
# print(p)
# print(p.__repr__())
print(p1*p2)
print((p1+p2).__repr__())
p1.__len__()
p2.__len__()
# print(len(e),"WEw")
# print(len(p1))
# print(len(p2))
# len(p2)