# n!= 1 X 2 X3 X 4.....Xn
# n!= [1 X 2 X3 X 4.... Xn-1] Xn
# n!= (n-1)! Xn
# n!= n X (n-1)!
def fact_iter(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    # print("The factorial of ",num,"is :",fact)   
    print(f"The factorial_iterative of  {num} is : {fact}") 

def fact_rec(num):
    if(num<2):
        return 1
    else:
        return num *fact_rec(num-1) 

num=int(input("Enter the number:"))
fact_iter(num)
print(f"The factorial_recursive of  {num} is : {fact_rec(num)}")

# Recursion infinite loop condition cause stack overflow problem so please be careful while working with recursion..