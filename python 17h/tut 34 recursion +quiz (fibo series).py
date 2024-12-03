"""factorial by iteration"""
"""YOU can easily debbug Iterative complex function but sometimes its code is lengthy."""
# def factorial_iterative(n):
#     """
#       n!=n * n-1 * n-2 * n-3.......1
#       n!=n*(n-1)!
#       :param n:integer
#       :return:n*n-1*n-2*n-3.......1
#       """
#     fac = 1
#     for i in range(n):
#      fac=fac*(i+1)
#     return fac
#     # pass
# number=int(input("Enter a number:"))
# print(factorial_iterative(number))

"""factorial by recursion."""
"""Their is little difficult to debbug recursion complex function but its code is small."""
def factorial_recursive(n):
  if n==1 or n==0:
      return 1
  else:
      return n*factorial_recursive(n-1)
# 5 * factorail_recursive(4)
# 5 * 4 *factorail_recursive(3)
# 5 * 4 * 3 *factorail_recursive(2)
# 5 * 4 * 3 * 2factorail_recursive(1)
# 5 * 4 * 3 * 2 *1 = 120
number=int(input("Enter a number:"))
print(factorial_recursive(number))

#quiz (print fibo series)
# # 0 1 1 2 3 5 8 13
# def fibo(n):
#     # if index start with 0
#   # if n==0 or n==1:
#   #     return n
#     # if index start with 1
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#       return fibo(n-1)+fibo(n-2)
#
# number=int(input("Enter a number:"))
# print(fibo(number))