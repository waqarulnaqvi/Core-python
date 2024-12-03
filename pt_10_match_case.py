x=int(input("Enter the value of x: "))
# In python you can make more than one default cases.
# default case is like a else statement.
match x:#it is like Inhanced switch in java.
    case 0:
        print("x is zero ")
    case 1:
        print("x is one ")
    case _ if x<=80:#default case
        print("x is less than equal to 80 ")
    case _ if x!=95:#default case
        print("x is not equal to 90 ")
    case _:print("X is four")