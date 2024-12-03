from cgi import print_arguments


l1=[1,22,3,34,34,3,344]
# l1_sorted=l1.sort()#Wrong..
# print(l1_sorted)
# print(l1) 
# l1.sort() # sorts the list..
print(l1)
# l1.reverse()# reverses the list..
# print(l1)
# l1.append("hello world") # adds at the end of the list.. one of the most used function in the list..
# print(l1) 
# l1.append(420) # adds at the end of the list.. one of the most used function in the list..
# print(l1) 
l1.insert(l1.__len__()-1,1400) #Run.. #inserts 1400 at the last second index of the list..
l1.insert(l1.__len__(),1400) #Run.. #inserts 1400 at the last index of the list..
# l1.insert(2,34) #inserts 34 at index 2..
# l1.insert(3,234) #inserts 434 at index 3..
# print(l1)
# l1.insert(1222,434) #Run.. #inserts 434 at the last index of the list..
# print(l1)
# l1.pop(6) #removes element at index 6..
# l1.pop(5) #removes element at index 5..
# # l1.pop(10)#Error.. #IndexError: pop index out of range
# print(l1)
# l1.remove(22) # removes 22 from the list..
# l1.remove(21)#Error.. #ValueError: list.remove(x): x not in list
print(l1)

# for more detils or for more methods visit python official documentations..