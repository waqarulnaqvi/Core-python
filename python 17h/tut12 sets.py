#set
# to write set
# method 1:
# l=set({10,20})
# method 2:
# l=set([10,20])
# method 3:
# l={10,20}
l={10,20}
s=set()
s.add(1)
s.add(2)
s1=s.union({1,2,3})
s2=s.intersection({1,2,3})
print(s.isdisjoint(l))
# print(s)
# print(s1)
# print(s2)
print(len(s))
print(min(s2))
print(type(s1))
print(max(s1))
# set me value add karne ka tareeka (s.add(value))
s.add(1)#to add elements in a set.
s.add(1)#set only retain unique value and can't retain repeated value...
print(s)
# set me value remove karne ka tareeka (s.remove(value))
s.remove(2)
print(s)
# print(type(s))
#Method 1: store list in a set.
# s_from_list =set([1,2,3,4,5])
#Method 2:
l=[1,2,3,4,5]
s_from_list =set(l)
print(s_from_list)
print(type(s_from_list))
# we can write set in both way.
# Method:1
#k=set({1,2,3,4})
# Method:2
k={1,2,3,4}
print(type(k))
print(k)
k1=set([1,2,3,4])
print(type(k1 ))
print(k)
print(s.isdisjoint({2,3,4}))