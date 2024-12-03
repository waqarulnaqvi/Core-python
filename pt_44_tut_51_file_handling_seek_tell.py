# with open('myfile.txt') as f:
#     print(type(f))
#     # move to the 10th bit in a file.
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())
#
#     # read the next 5 bytes
#     data=f.read(5)
#     print

f=open("myt.txt" ,"w")
f.write("Hello world world")
f.truncate(7)

with open("myt.txt") as f:
    print(f.read())
