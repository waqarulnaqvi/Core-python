"""
# Exercise:5
Health Management System
# 3 clients- Harry,Rohan and Hammad
use this function:-
def getdate():
    import datetime
    return datetime.datetime.now()

Total 6 files (3 for diet 3 for exercise)
Write a functon that when executed takes as input client name
ex:-[time] cable crossover
One more function to retrieve exercise or food for any client.
When program start program asks you want to write or retrieve.
retrieve means to find information that has been stored.
"""
client=int(input("press 1 for write the information & press 2 for retrieve the information:"))
# client=1
def getdate():
    import datetime
    return datetime.datetime.now()
if client==1:
    w = int(input("press 1 to write in harry 2 to write in rohan press 3 to write in Hammad:\n"))
    if w == 1:
        f = open("tut 32 harry.txt","w")
        k=getdate()
        f.write("HARRY DIETCHART CHART")

        f.write("HARRY EXERCISE CHART")

        f.close()
    elif w == 2:
        with open("tut 32 rohan.txt", "w") as f:
            f.write("ROHAN DIETCHART CHART")

            f.write("ROHAN EXERCISE CHART")

            f.write(" \n")

    else:
        f = open("tut 32 hammad.txt", "w")
        f.write("HAMMAD DIETCHART CHART")

        f.write("HAMMAD EXERCISE CHART")

        f.write(" \n")
        f.close()
else:
    w = int(input("press 1 to read in harry 2 to read in rohan press 3 to read in Hammad"))
    if w == 1:
        with open("tut 32 harry.txt") as f:
            a = f.read()
            print(a)

    elif w == 2:
        f = open("tut 32 rohan.txt", "r+")
        a = f.read()
        print(a)
        f.close()
    else:
        f = open("tut 32 hammad.txt", "r+")
        a = f.read()
        print(a)
        f.close()






