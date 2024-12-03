"""Exercise:3
create a program capable of displaying questions to the user like KBC.
Use list data type to store the question and their correct answers.
Display the final amount the person is taking home after playing the game.
"""
# In python list = arrays and objects = dictionary.
questions=[
    ["a. Which language was used to create fb?","Python","French","Java","None",4],
    ["b.Who is the prime minsiter of India?", "Python", "French", "Java", "None", 4],
    ["c.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["d.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["e.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["f.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["g.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["h.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["i.Which language was used to create fb?", "Python", "French", "Java", "None", 4],
    ["j.Which language was used to create fb?", "Python", "French", "Java", "None", 4]]
# print(f"Question for Rs. {levels[i]} \n{questions[i][i][i]}") #In python this is also valid.
# print(f"Question for Rs. {levels[i]} \n{questions[i][i]}") #In python this is also valid.
# print(f"Question for Rs. {levels[i]} \n{questions[i]}") #In python this is also valid.
print("****************WELCOME TO KBC****************\n")
levels=[1000,2000,3000,5000,10000,20000,40000,80000,100000,160000,320000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    # print(f"Question for Rs. {levels[i]} \n{questions[i][i][i]}")#valid print a
    # print(f"Question for Rs. {levels[i]} \n{questions[i][i]}")#valid
    print(f"Question for Rs. {levels[i]} \n{question[0]}")#same
    # print(f"Question for Rs. {levels[i]} \n{questions[i][0]}")#same

    print(f"1.{question[1]}  2.{question[2]}")
    print(f"3.{question[3]}  4.{question[4]}")
    reply=int(input("Enter your answer (1-4) or 0 to quiting from the game:\n"))

    if(reply == question[-1]):
       print(f"Correct answer,you have won Rs. {levels[i]}\n")
    elif(reply ==0):
        print(f"Quiting from the game!!")
        # return #SyntaxError: 'return' outside function
        # exit() #exit function is like return statement in java it will exit user from the entire program.
        break
    else:
        print("Wrong answer!!")
        break
        # exit() #exit function is like return statement in java it will exit user from the entire program.
        # print(f"You won {levels[i-1]}")

    if(i==3):
        money=levels[i]
    elif(i==7):
        money=levels[i]
    elif(i==len(questions)-1):
        money=levels[i]

print("Money Won : {}".format(money))


