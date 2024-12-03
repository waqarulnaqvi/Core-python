# Importing a module is a processing of loading code from python module into the current script.
# import pandas
# pandas.read_csv()
#
# import math
# print(math.floor(4.2323))
# print(math.sqrt(9))
#
# # when you wish to import only sqrt and pi from math package/module or selective math functions.
# from math import sqrt,pi
# result =sqrt(12) *pi
# # print(result)
#
# from math import *
# print(sqrt(34*pi))
# # 10 55
# from math import * #all the functions within math module/package will be available in the class.
# #it is not recommended approach because it can lead to confusion and make it harder to understand where specific functions and variables are coming from..
# # result =sqrt(12) *pi
# # print(result)
# # result =max(23,3) * sqrt(12) *pi
# # print(result)
#
# from math import pi,sqrt as s
# import math as m
#
# print(s(4 ))
# print(m.sqrt(4))
# print(m.floor(34734.3434))

import math as math_builtin_python
result=math_builtin_python.sqrt(34)*math_builtin_python.pi
print(result)

# from waqarul import * as s #it will throw an error.
# from waqarul import *
# from waqarul import waqarul,welcome
# import math
# # print(dir(math))
# print(math.nan,type(math.nan))
# welcome()
# print(waqarul)

import waqarul as w
print(w.waqarul)
w.welcome()


