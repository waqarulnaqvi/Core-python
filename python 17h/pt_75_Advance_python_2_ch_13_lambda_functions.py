# def func(a):
#     return a+5

func = lambda a: a+5
# yha pe humme function as an argument pass karna hota hai un cases me hum lambda function use karte hai..

"""lambda functions :
functions created using an expression using lambda keyword..
Syntax :
lambda arguments:expressions 
                    |
                    >Can be used as a normal functions.. 

lambda function is also called as an anonymous function..
"""
# lambda function is a one liner function..you can not write every function (like complex funtion) in the form of the lambda but you can write simple function in the form of the lambda function(one liner funtion)..

square =lambda x:x*x
sum =lambda a,b,c:a+b+c

x=566
print(func(x))
print(square(2))
print(sum(1,2,3))