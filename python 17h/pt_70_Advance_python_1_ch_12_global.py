a=54 #Global variable..
def fun():
    global a #it changes global variable value..
    print(a)
    a=8 #Local variable..
    print(a)
    # global a #Error.. 
    # print(a) #Error..

fun()
print(a)