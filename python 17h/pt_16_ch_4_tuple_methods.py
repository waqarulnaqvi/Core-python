# Creating a tuple using ()..
t=(1,2,4,5,1,1,1,1)
print("Using Count Function:")
print(t.count(1))
print(t.count(3))
print(t.count(2))

print("Using Index Function:")
print(t.index(1))
# print(t.index(3))#Error..#ValueError: tuple.index(x): x not in tuple
print(t.index(2))
print(t.index(5))