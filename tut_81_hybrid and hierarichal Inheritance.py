# Example of Hybrid Inheritance:
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass

# Example of Hierarichal Inheritance:
# Hierarichal Inheritance is tree like a Structure:
class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass

class D4(D1):
    pass

class D5(D2):
    pass

class D6(D2):
    pass