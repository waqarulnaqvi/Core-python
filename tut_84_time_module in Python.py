# 11 12
# 12 :7
# 11 24
import time

def usingWhile():
    i=0
    while i<50000:
        i=i+1
        print(i)


def usingFor():
    for i in range(50000):
       print(i)
       if i == 2800:
           break

# iniit=time.time()#return the current time in seconds
# usingFor()
# print("Total time used by for loop: ",time.time()-iniit)

# init=time.time()#return the current time in seconds
# usingWhile()
# print("Total time used by while loop: ",time.time()-init)

# print(4)
# t1=time.sleep(3)
# # print(f"This is printed after 3 second : {time.sleep(3)}")
# print(f"This is printed after 3 second : {t1}")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)