"""TASK 4:
Rock-Paper-Scissors Game
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback

"""
import random
class Rock_Paper_Scissors:
    def computer_choice(self):
        num = random.randint(1, 3)
        return num
    def game(self,c_choice,u_choice):
        c=0
        match u_choice:
            case 1:
                if c_choice==u_choice:
                    print("Draw")
                elif c_choice==3:
                    print("Computer win")
                    c=c-1
                else:
                    print("YOU win")
                    c=c+1

            case 2:
                if c_choice==u_choice:
                    print("Draw")
                elif c_choice<u_choice:
                    print("Computer win")
                    c=c-1
                else:
                    print("YOU win")
                    c=c+1

            case 3:
                if c_choice==u_choice:
                    print("Draw")
                elif c_choice==1:
                    print("Computer win")
                    c=c-1
                else:
                    print("YOU win")
                    c=c+1
        return c

r_p_s=Rock_Paper_Scissors()
sum=0
while True:
    comptr_choice=r_p_s.computer_choice()
    user_choice=int(input("Enter\n1 for Rock\n2 for scissor\n3 for paper\nEnter any other key to exit the game:\n"))
    if user_choice<1 or user_choice>3:
        break
    dict={1:"Rock",2:"Scissor",3:"Paper"}
    sum+=r_p_s.game(comptr_choice,user_choice)
    print(f"Your choose :{dict.get(user_choice)}\nComputer choose :{dict.get(comptr_choice)}\n")

if sum>0:
    print("RESULTS:\n***************YOU WIN***************")
elif sum==0:
    print("RESULTS:\n***************DRAW***************")

else:
    print("RESULTS:\n***************COMPUTER WIN***************")

# num2=random.randrange(9,10)
# print(num2)