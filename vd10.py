# Best use case of lambda function
cube=lambda x:x**3

def app(fx,value):
    return value +fx(value)


print(app(cube,6))
print(app(lambda x:x**2,6))