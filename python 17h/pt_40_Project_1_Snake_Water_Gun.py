"""Project 1:(Snake,Water,Gun Game or Rock,paper,scissors)
We all have played snake,water, gun game in our childhood .If you haven't ,google the rules of the game and write a Python program capable of playing this game with the user..
"""
import random #random is a module in python..
def gameWin(comp,you):
    if comp==you :
        return None
    elif comp =='s':
        if you == 'w':
            return False
        if you =='g':
            return True
    elif comp =='w':
        if you =='g':
            return False
        if you =='s':
            return True
    elif comp =='g':
        if you =='s':
            return False
        if you =='w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)#randint is a function in random module in python..
# print(randNo)
if randNo ==1:
    comp ="s"
elif randNo ==2:
    comp ="w"  
elif randNo ==3:
    comp='g' 

you =input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a=gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if gameWin(comp,you)==None:
    print("The game is a tie!")
elif gameWin(comp,you):
    print("You Win!")
else:
    print("You Lose!")        