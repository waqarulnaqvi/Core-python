# 12 11
# Magic method purpose to do some special task.
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i + 1
#         return i

# Half code in emp.py file
from emp import Employee
e=Employee("Waqar8ul")
print(e.name)
print(len(e))
print(e)
print(repr(e))
print(e.__str__())
print(e.__repr__())
print(str(e))
# e()
# Quick Quiz
print(e())