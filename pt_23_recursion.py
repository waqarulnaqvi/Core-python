def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def fib(n):#when index starts with 0
    if n <= 1:
        return n
    else:
        return fib(n-1)+ fib(n-2)

def fib1(n):#when index starts with 1
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fib1(n-1)+ fib1(n-2)

# print(fact(5))
# print(fact(4))
# print(fact(3))
print(fib(3))
print(fib1(2))
print(fib1(5))
print(fib(6))
print(fib1(5))