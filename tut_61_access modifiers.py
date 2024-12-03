"""Types of access Specifiers:
All the methods in python are by default public.Any instance variable in a class followed by the 'self' keyword ie.
self.var_name are public accessed.
1.Public access specifiers
2.Private access specifiers
1.Protected access specifiers
"""
class Employee:
    def __init__(self,name,id,address):
        self.name=name #by default it is publi                                                                                                                                                                       vc #it can be easily accessible.
        self.__id=id#it become private.  (mangling occur only when we use a __(double underscore)) #it can not be easily accessible.
        self._address=address#it become protected. #it can be easily accessible.

    def show(self):
        """Name Mangling:
        Name Mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidently overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively."""
        print(f"The name is {self.name} and id is {self._Employee__id} and address is {self._address}")
e=Employee("waqar",2323,"lucknow")
print(e.name)
# print(e.id)#Can not be accessed directly  because it is private.
print(e._Employee__id)#Can be accessed indirectly # This process is called name mangling in python.
e.show()
print(dir(e))#same.
print(e.__dir__())#same.
# e.show()
