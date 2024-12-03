#you should assure that python file name didn't match with module
'''i=0
while (True):#while(True): or while (1): ek esa while loop hota hai jo hamesha chalta hi rehta hai
    i=i+1
    if i+1<5:
        i+=1
        continue
    print(i+1 ,end=" ")
    if i==45:
        break
    i+=1'''
#quiz:
while 1:
    inp=int(input("Enter a number greater than 100:"))
    if inp<=100:
        print("Please Enter a number greater than 100")
        continue
    else: #else statement is redundent here.
        print("Congratulation aap ne 100 se bada number print kar diya")
        break
