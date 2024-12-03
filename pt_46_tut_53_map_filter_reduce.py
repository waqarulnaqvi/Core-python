cube=lambda x:x**3
# 12 15
# print(cube(2))

# Map filter and reduce are a higher order function because they can take function as an function argument.
l= [1,2,4,6,4,3]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)
#
# "MAP"
newl=list(map(cube,l))
print(newl)
print(l)
#
# "FILTER"
def filterrr(a):
    return a>2

newnl=list(filter(filterrr,l))#jin jin value ke liye yeah values aapke function me rahengi unke liye yeah function true return karega wahi value rahengi baaki values ni rahengi or un values ke liye yeah function false return karega.
print(newnl)

newn=list(filter(lambda x:x<6,l))
print(newn)

"reduce"
from functools import reduce

numbers=[1,2,3,4,5]
sum=reduce(lambda a,b:a*b,numbers)
#reduce function can only take two positional arguments not more or less than that.
print(sum)
