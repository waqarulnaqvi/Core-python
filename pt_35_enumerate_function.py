marks =[12,23,100,43,67,88,0]
# linter in python means the errors which is obivious.

# Method :1
# index=0
# for mark in marks:
#     print(mark)
#     if (index==len(marks)-1):
#         print("Zero marks")
#     index+=1

for index,mark in enumerate(marks):
    print(mark)
    if (index==2):
        print("Full marks")
print()

for index,mark in enumerate(marks,start=1):
    print(mark)
    if (index==2):
        print("Full marks")
