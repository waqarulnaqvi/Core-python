# IN  FUCTION CACHING VALUES CAN BE MEMOIZE
# MEMOIZE MEANS To store so that it can be susequently retrived without repeating the computation.
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def function(n):
    time.sleep(5)
    return n*5

print(function(30))
print("done for 30")
print(function(30))
print("done for 30")
print(function(3))
print("done for 3")
print(function(2))
print("done for 2")
print(function(30))
print("done for 30")
print(function(20))
print("done for 20")