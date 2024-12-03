'''
There are four types of arguments that we can provide in a function:
1)Default arguments
2)Keyword arguments
3)Variable  length arguments
4)Required  arguments
'''

def average(a=1,b=2):#default arguments
    print("Average is : ",(a+b)/2)

def average1(a,b=2):#a is Required arguments
    # return 1211  # if there are 2 returns are there in the program then python interpretor use only the first one .
    return (a+b)/2 #return ka matlab wapas chale jao us value ko leke


def average11(a,b=2):#a is Required arguments
    pass

def average2(*numbers):#Variable  length arguments
    print(type(numbers))#we will take numbers as an tuples here.
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ",sum/len(numbers))

def name(**name):
    print(type(name))#we will take name as an dictionary here.
    print("Hello, ",name["fname"],name["mname"],name["lname"])

name(mname="Buchanan",lname="Barnes",fname="James")
# average()
# average(34,4)
# average(34)
# average(b=34)
# average(a=34)

#In keyword arguments we will change the order.
average(b=213,a=34)

#Required arguments wo hote jo aapko dene hi dene hai
# average1() #Error ek value dena hi dena hogi because one arguement in average1 function is a required arguments
c=average1(12)
print("Average is 11: ",c)
print("Average is 22: ",average1(1,9))
print("Average is 21: ",average11(1,9))
average2(2,3,42,2)