# Assignment 20 (dictionary)
# Problem :1
def get_key(values):
    for key,value in dict.items():
        if values ==value:
            return key

dict={'Red': 10, 'Green': 41, 'White': 22, 'Black': 3, 'Pink': 14, 'Yellow': 5}
values=list(dict.values())
values.sort()

sorted_dict={get_key(i):i for i in values}
print(sorted_dict)

values.reverse()
des_sorted_dict={get_key(i):i for i in values}
print(des_sorted_dict)

# Problem :2
# dict={}
# dict["key"]="value"
# print(dict)

# Problem:3
# def new_dic(dict,*dicts):#it allow pass multiple argument as a tupple inside a function
#     for i in dicts:
#         dict.update(i)
#     return dict
#
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dict4={}
# print(new_dic(dict4,dic1,dic2,dic3))#multiple argument as a tupple inside a function

#Problem:4
# dic1={1:10,2:20}
# if 2 in dic1:
#     print("TRUE")
# else:
#     print("FALSE")

# Problem:5
# dic1={1:10,2:20}
# for i in dic1:
#     print(i ,":", dic1.get(i))

# Problem:6
# inp=input("Enter the n value:")
# dict={}
# for i in range(1,int(inp)+1):
#     dict[i]=i*i
# print(dict)

# Problem:7
# def function():
#     dict={}
#     for i in range(1, 16):
#         dict[i] = i * i
#     return dict
#
# print("The value of dictionary is :",function())


# Problem:8
# def new_dic(dict,*dicts):
#     for i in dicts:
#         dict.update(i)
#     return dict
#
# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dict4={}
# print(new_dic(dict4,dic1,dic2))

# Question:9
# dict={"abc":1,1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
# su=sum(dict.values())
# print("Sum of dictionary element is :",su)

# # Question:10
# def list_to_dict(keys,values):
#     dict={}
#     for key,value in zip(keys,values):
#         dict[key]=value
#     return dict
# Samplelist=['Red','Green',"White","Black","Pink","Yellow"]
# l1=[0,1,2,3,4,5]
# print("Merging 2 lists and making a dictionary :",list_to_dict(Samplelist,l1))

