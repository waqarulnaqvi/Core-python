# Question:1
# l1=[1,2,4,5,6,7]
# sum=0
# for i in l1:
#     sum+=i
# print("sum of element in a list is :",sum)

# Question :2
# l1=[1,2,4,5,6,7]
# mul=1
# for i in l1:
#     mul*=i
# print("Multiplication of element in a list is :",mul)

# Question :3
# l1=[1,2,41,5,6,7]
# max=-23232323
# for i in l1:
#     if i>max:
#         max=i
# print("Maximum element in a list is :",max)

# Question :4
# l1=[2,41,5,1,6,7]
# min=23232323
# for i in l1:
#     if i<min:
#         min=i
# print("Minimum element in a list is :",min)

# Question :5
# def  count_string(list):
#     c=0
#     for i in list:
#         if isinstance(i,str):
#             c+=1
#     return c
# list=["hello","Yellow",True,3,"abc",232,None,False,"billo"]
# print(f"Total no of string is {count_string(list)}")

# Question :6
# def  count_string(list):
#     c=0
#     for i in list:
#         if isinstance(i,str) and len(i)>=2 and i[0]==i[-1]:
#             c+=1
#     return c
#
# list=["hello","Yellow",True,3,"aba",232,None,False,"billo","a","abihiiia","abba"]
# print(f"Total no of string is {count_string(list)}")

# Question :7
# def duplicate_ele(list):
#     for i,a in enumerate(list):
#         for j,b in enumerate(list):
#             if i!=j and a==b:
#                 # list.remove(a)
#                 list.pop(i)
#                 break
#     return list
# def extract_list(list):
#     for i in list:
#         print(i,end="\t")
#
# list=["abc",12,True,False,"cat",None,True,False,None ,"cde","cde",12,3434]
# print("Original list :")
# extract_list(list)
#
# duplicate_ele(list)
# print("\n\nUpdated list :")
# extract_list(list)

# Question :8
# list=["abc",12,True,False,"cat",None,True,False,None ,"cde","cde",12,3434]
# if not list:
#     print("The list is empty!!")
# else:
#     print("The list is not empty!!")

# Question :9
# def take_2_list(l1,l2):
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 return True
#     return False
# print("The list have atleast 1 common element ",take_2_list([1,44,6,2,433],[2,2,3,43,3]))

# Question :10
# l1=[0,1,2,3,4,5,6,7]
# l2=[]
# for  i,j in enumerate(l1):
#     if i==0 or i==4 or i==5:
#         continue
#     else:l2.append(j)
#
# print(l2)
# 22 24
# Question :11
Samplelist=['Red','Green',"White","Black","Pink","Yellow"]
Expectedlist=[]
for j in Samplelist:
    if j=="Yellow" or j=="Red" or j=="Pink" :
        continue
    else:
        Expectedlist.append(j)

print("Expected Output :",Expectedlist)

# Question :12
# l1=[1,2,2,222,44,347]
# l2=[]
# for  i in l1:
#     if i%2!=0:
#         l2.append(i)
#
# print(l2)
