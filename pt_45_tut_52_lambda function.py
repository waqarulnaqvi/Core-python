def double(x):
    return x*2

double_ag=lambda x:x*2

cube=lambda x:x**3

avg=lambda x,y=3: (x+y)/2

# passing function as an value In the case lambda function is most used and actually it is the best use case of the lambda function.
def app(fx,value):
    return value +fx(value)

# print(double(5))
# print(double_ag(5))
# print(cube(5))
# print(avg(3,5))
print(app(cube,6))
print(app(lambda x:x**2,6))#In this case this lambda function does not have any name that is why it is also called as anonymous function.
#this is the main use case of the lambda function when we are passing function as an argument.