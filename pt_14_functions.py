def Gmean(a,b):#function definition
    mean=(a*b)/(a+b)#function declaration
    print(mean)#function declaration

def isGreate(a,b):
    pass #if we want to define function body and function declaration later than we can use a pass and define it later

while(True):
    i=int(input("Enter a number 1:"))
    if(i==0):
        break
    j=int(input("Enter a number 2:"))
    Gmean(i,j)
