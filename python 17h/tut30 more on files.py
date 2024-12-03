f=open("tut 26.txt")
print(f.tell())#it tells where your file pointer is.
print(f.readline())
print(f.tell())#it tells where your file pointer is.
f.seek(10)#it returns/jump the file pointer to the your wish position.ex:- file pointer return to the 10th.
print(f.readline())
print(f.tell())#it tells where your file pointer is.
# Quiz:-Kya galti hai minute si program me.
# soln:-file close ni ki hai f.close() function lagake.
f.close()