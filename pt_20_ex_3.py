"""Exercise:3
create a program capable of displaying questions to the user like KBC.
Use list data type to store the question and their correct answers.
Display the final amount the person is taking home after playing the game.
"""
# In python list = arrays and objects = dictionary.
print("1.Who is the prime minsiter of India ?")
print("1)Narendra Modi")
print("2)Narendrrra kodi")
print("3)Marendra Modi")
print("4)sarendra Modi")
ans=int(input())
'''Method :1'''
if ans ==1:
    print("Correct")
    print("1000 price money")
else:
    print("Wrong")
    print("0 price money")
    exit()

print("\n2.What is the first prime minsiter of India ?")
print("1)Narendra Modi")
print("2)jawaharlal nehru")
print("3)Marendra Modi")
print("4)sarendra Modi")
ans=int(input())

if ans ==2:
    print("Correct")
    print("10000 price money")
else:
    print("Wrong")
    print("1000 price money")

'''Method:2
if ans ==1:
    print("Correct")
    print("1000 price money")
    
    print("\n2.What is the first prime minsiter of India ?")
    print("1)Narendra Modi")
    print("2)jawaharlal nehru")
    print("3)Marendra Modi")
    print("4)sarendra Modi")
    ans = int(input())

    if ans == 2:
        print("Correct")
        print("10000 price money")
    else:
        print("Wrong")
        print("1000 price money")
else:
    print("Wrong")
    print("0 price money")
'''