# 6 15
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)

    # def area(self):
    #     return 3.14*self.r    
    # 
    def area(self):
        print("Area of rectangle",super().area())
        return 3.14*super().area()

    @classmethod
    def fromStr(cls,x):
        return

sqr=Shape(34,4)
print(sqr.area())
c=Circle(5)
print(c.area())