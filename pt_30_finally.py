def func1():
    try:
        list=[1,2,43,34,34]
        index=int(input("Enter the index:"))
        print(list[index])
        return 1
    except :
        print("Some Error occured!")
        return 0
    finally:
        print("I am always executed!!")
    # print("I am in function that's why I will not executed!!")

a=func1()
print(a)

a=0
try:print(5/a)
# except Exception as e:
#     print(e)
finally:
    print("When we are not in the function then finally does not have any value below code will always executed!!")
    print("Finally has value only when you use try with finally when you are not in the function")
print("When we are not in the function then finally does not have any value below code will always executed!!")