# a=True
# print(a:=False)#It allows you to assign a value within a expression.
# # It can be used in a while loop as well as in a if statements
# print(a)
# numbers=[1,2,3,4,5]
# while(n:=len(numbers)) >0:
#     print(numbers.pop())
#     print(n)

"""
walrus operator :=

new to Python 3.8
assignment expression aka walrus
operator
assigns values to variables as part of a larger  expression
"""
happy=True
print(happy)

print(happy:=True)

foods=list()

# while True:
#     food= input("What food do you like?:")
#     if food == "quit":
#         break
#     foods.append(food)

while (food:=input("What food do you like? ")) !="quite":
    foods.append(food)

print(food)
print(foods)

