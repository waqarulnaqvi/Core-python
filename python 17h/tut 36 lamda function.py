# lambda functions or anonymous functions
# METHOD 1:
# def minus(x,y):
#     return x-y
# print( minus(2,34))
# METHOD 2:
minu =lambda x,y:x-y
print( minu(2,34))

# METHOD 1:
def first(a):
    return a[1]
def firs(a):
    return a[-1]
a=[[1,4],[133,-5],[22,3]]
# method a:
a.sort(key=first)
print(a)
# method b:
a.sort(key=firs)
print(a)
# METHOD 2:
a=[[1,4],[133,-5],[22,3]]
# method a:
a.sort(key=lambda x:x[-2])
print(a)
# method b:
a.sort(key=lambda x:x[0])
print(a)
