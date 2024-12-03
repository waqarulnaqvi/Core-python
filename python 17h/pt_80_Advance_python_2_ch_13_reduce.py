# from functools import reduce

# sum=lambda a,b :a+b

# l=[1,2,3,4]
# val=reduce(sum,l)
# print(val)

# print sum of n natural number:
from functools import reduce

sum=lambda a,b :a+b
n=int(input("Enter a number:"))
l=[i for i in range(1,n+1)]
print(l)
print(reduce(sum,l))