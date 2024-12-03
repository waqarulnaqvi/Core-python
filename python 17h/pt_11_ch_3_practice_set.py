# In python keywords and variables are case sensitive..
# problem 2:
# letter="""
# Dear <|NAME|>,
# Greetings from ABC coding house.I am happy to tell you about your selection.
# You are selected!
# Have a great day ahead!
# Thanks and regards,
# Bill.
# Date: <|DATE|>
# """
# print(letter)
# name=input("Enter your name:\n")
# date=input("Enter Date:\n")
# letter=letter.replace("<|NAME|>",name)
# letter=letter.replace("<|DATE|>",date)
# print(letter)

# problem 3:
# st="This is a String with double  spaces!"
# doubleSpaces=st.find("  ")
# print(doubleSpaces)

# problem 4:
# st="This is a String with double  spaces!"
# print(st)
# # doubleSpaces=st.replace("  "," ")
# # print(doubleSpaces)
# # print(st)
# st=st.replace("  "," ")
# print(st)

# problem 5:
letter="Dear Harry,This Python course is nice!.Thanks!"
print(letter)
formatted_letter="Dear Harry,\n\tThis Python course is nice!.\nThanks!"
print(formatted_letter)