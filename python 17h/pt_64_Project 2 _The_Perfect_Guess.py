"""Project 2 - The Perfect Guess
We are going to write a program that generates a random number and asks the user to guess it.
If the player guess is higher than the actual number,the program displays "Lower number please".
Similarly if the user's guess is too low, the program prints "higher number please"..When the user
 guides the correct number,the program displays the number of guesses the player used to arrive at the number.

 Hint :use the random module.. 
"""
"""MY LOGIC:
import random
rnd=random.randint(1,10)
# print("Generated number is: "+str(rnd))
attempt=1
while(True):
    i=int(input("Guess the number between 1 to 10:\n"))
    if(i>rnd):
        print("Lower number please..")
        attempt=attempt+1
    elif(i<rnd):
        print("Higher number please..")
        attempt=attempt+1
    else:
        if attempt==0:
            print("The Perfect Guess!")
        else:
            print("You Finally guess the number!") 
        break
print("Total Number of attempt: "+str(attempt))
"""

"""CWH LOGIC:"""
import random
from warnings import catch_warnings
rnd=random.randint(1,10)
print("Generated number is: "+str(rnd))
i=None
attempt=1
while(i!=rnd):
    i=int(input("Guess the number between 1 to 10:\n"))
    if(i>rnd):
        print("Lower number please..")
        attempt=attempt+1
    elif(i<rnd):
        print("Higher number please..")
        attempt=attempt+1
    else:   
        print("The Perfect Guess!")
        
print("Total Number of attempt: "+str(attempt))
      
"""Method:1"""
with open("hiscore.txt","r" )as f:
        try:
            hiscore =int(f.read())
            # print(hiscore)
        except Exception as e:
            hiscore=1000000 
            # print(e)        

"""Method:2
try:
    with open("hiscore.txt","r" )as f:
       hiscore =int(f.read())
    #    print(hiscore)
except:
    hiscore=1000000
    # print(e) #Error because e is not defined..
"""     

if(attempt<hiscore):
    print("You have just broken the high score!") 
    with open("hiscore.txt","w") as f:
        f.write(str(attempt))   
        
