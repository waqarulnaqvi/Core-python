# 7 22
# with open ('myfile.txt') as f:
#     while True:
#
#         line=f.readline()
#         print(line,end="")
#         if not line :
#             print(line,type(line))
#             break
#         # print(line)


# f= open('myfl.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         # print(line)
#         # print("ere")
#         break
#     m1= int(line.split(",")[0])
#     m2= int(line.split(",")[1])
#     m3= int(line.split(",")[2])
#     print(f"Marks of student {i} in Maths is: {m1}")
#     print(f"Marks of student {i} in Maths is: {m2}")
#     print(f"Marks of student {i} in Maths is: {m3}")
#     print(line)

with open('myfe.txt','w')as f:
    lines=["ab\n","bc\n","cd\n","de\n"]
    f.writelines(lines)

