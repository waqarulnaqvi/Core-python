# 9 12
# It is a good example of the encapsulation.
class MyClass:
    def __init__(self,values):
        self._value=values

    def show(self):
        print(f"value is {self._value}")

    @property
    def value1(self):
        return 10*self._value

    @value1.setter
    def value1(self,value):
        self._value=value


obj=MyClass(11)
obj.show()
print(obj.value1)
# obj._value=34
print(obj.value1)
obj.value1=18782
print(obj.value1)