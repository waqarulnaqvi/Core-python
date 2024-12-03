"""Exercise : 4
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end.
else:
simply reverse the string

Decoding:
 if the word contains less than 3 characters, reverse it
else:
remove 3 random characters from start and end.Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode
"""

'''
word="alpha male"
# print(word[::-1])
# print(word[-1] +word[:-1])
'''
# print(__doc__)
# dec=enc=0
"""
def code(str):
    run=True
    words = str.split(" ")
    while run:
        # words = str.split(" " and "/") # consider only "/" and does not consider " "
        # words = str.split(" " or "/")  # consider only " " and does not consider "/"
        nwords = []  # it is a list and we are storing words in a list.
        # run=input("1 for coding or 0 for Decoding")
        # run=True if run=="1" else False
        # run=1 if run=="1"  else exit()
        code = int(input("Enter 1 for encoding\nEnter 2 for decoding\nEnter any key to change the message: \n"))

        match code:  # it is like Inhanced switch in java.
            case 1:
                for word in words:
                    # print(word)
                    if len(word) >= 3:
                        rand = "".join(random.sample(concanitate, length))
                        rand2 = "".join(random.sample(concanitate, length))
                        stnew = rand + word[1:] + word[0] + rand2
                        nwords.append(stnew)  # append stnew (String) in a nwords list.
                    else:
                        nwords.append(word[::-1])

                print(" ".join(nwords))  # join method joining the list element in the string.
                words=nwords
                # return nwords

            case 2:
                # for word in words:
                #     if len(word) >= 3 and len(word) <= 8:
                #         print("The sentence is not in decoded form \n")
                #         # continue
                #         # exit()
                #         break
                        # return "sorry"
                for word in words:

                    if len(word) >= 3 and len(word) <= 8:
                        print("The sentence is not in decoded form!")
                        # continue
                        # exit()
                        break

                    if len(word) >= 3:
                        stnew = word[3:-3]
                        stnew = stnew[-1] + stnew[:-1]
                        # k=stnew[-1:-1 ] #wrong.
                        # print(k)
                        # print(stnew)
                        nwords.append(stnew)  # append stnew (String) in a nwords list.
                        words = nwords
                    else:
                        nwords.append(word[::-1])  # reversing a word(string) and appending in nwords list.
                        words = nwords
                print(" ".join(nwords))  # join method joining the list element in the string.

                # return nwords
            case _:
                # exit()
                run=False
                print("Exiting from the loop!!")


# def encode_decode(new_list,str,wish):
#     if new_list !="sorry":
#         new_string = " ".join(new_list)
#         if wish == "1":
#             str=new_string
#             code(str)
#     else:
#         code(str)

import random
lower="abcdefghijklmnopqrstuvwxyz"
Upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
concanitate=lower+Upper
length=3
run=True
while run:
    str = input("Enter String:")
    code(str)
    inp = input("Do you want to continue? \n 1 for continue \n 2 for exit:\n ")
    run = True if inp == "1" else False
    # wish = "1"
    # while wish=="1":
    #     wish = input("\ndo you wish to encode/decode the same String or not \nEnter 1 for encode/decode \npress any key to exit\n")
    #     encode_decode(new_list, str, wish)
"""

"""Exercise : 4
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end.
else:
simply reverse the string

Decoding:
 if the word contains less than 3 characters, reverse it
else:
remove 3 random characters from start and end.Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode
"""
import string
import random
class Coding_Decoding:
    def __init__(self,str):
        self.str=str
        # self.lower = "abcdefghijklmnopqrstuvwxyz"
        # self.Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # self.concanitate = self.lower + self.Upper
        # self.concanitate=string.ascii_lowercase+string.ascii_uppercase
        self.concanitate=string.ascii_letters
        # print(string.ascii_uppercase)
        # print(string.ascii_lowercase)
        # print(string.ascii_letters)
        # print(string.__all__)
        self.strr=""
        self.layer=0

    def Coding(self):
        self.starting_rand_alp="".join(random.sample(self.concanitate,3))
        # self.starting_rand_alp="".join(random.choices(self.concanitate,k=3))
        # print(self.starting_rand_alp)
        self.ending_rand_alp="".join(random.sample(self.concanitate,3))
        # print(self.ending_rand_alp)
        self.strr=""
        self.layer+=1
        strlist=self.str.split(" ")
        # print("/ /".join(strlist))
        # print(strlist)
        for word in strlist:
            if  len(word) < 3:
                 self.strr+=word[: :-1]+" "
                 # print(word[: :-1],end=" ")
            else:
                self.strr+=self.starting_rand_alp+word[1:]+word[0]+self.ending_rand_alp+" "
        print(f"Original Message is : {self.str}")
        print(f"{self.layer} layer Encoded Message:")
        print(self.strr,end="\n\n")
        self.str=self.strr
        # print(self.str+"hello")

    def Decoding(self):
        if self.layer==0:
            print("The Message is already in Decoded format!!")
            print("Already Decoded Message is:")
            print(self.strr, end="\n\n")
        else:
            decodedstr = self.strr.split(" ")
            self.strr = ""
            # print(decodedstr)
            for word in decodedstr:
                # print(word)
                if len(word) < 3:
                    self.strr += word[::-1] + " "
                else:
                    self.strr += word[-4] + word[3:-4] + " "
            self.layer -= 1
            print("The Decoded Message is:")
            print(self.strr, end="\n\n")
            print(f"Total layer that need to be decoded is {self.layer} ")
            self.str = self.strr

    # def Decoding(self):
    #     for word in self.strr:
    #         if len(word) >= 3 and len(word) <= 8:
    #             print("The Message is already in Decoded format!!")
    #             print("Already Decoded Message is:")
    #             print(self.strr, end="\n\n")
    #             break
    #     if self.strr=="":
    #         self.strr=str
    #     decodedstr = self.strr.split(" ")
    #     self.strr = ""
    #     # print(decodedstr)
    #     for word in decodedstr:
    #         # print(word)
    #         if len(word) < 3:
    #             self.strr += word[::-1] + " "
    #         else:
    #             self.strr += word[-4] + word[3:-4] + " "
    #     if self.layer!=0:
    #         self.layer -= 1
    #     print("The Decoded Message is:")
    #     print(self.strr, end="\n\n")
    #     print(f"Total layer that need to be decoded is {self.layer} ")

    def display(self):
      while True:
        code = int(input("Enter 1 for encoding\nEnter 2 for decoding\nEnter any key to change the message :\n"))
        match code:  # it is like Inhanced switch in java.
            case 1:
                self.Coding()
            case 2:
                self.Decoding()
            case _:
                break

run=True
while run:
    word = input("Enter a Message that you want to encode/decode:\n")
    cd = Coding_Decoding(word)
    cd.display()
    inp = input("Do you want to continue? \n 1 for continue \n 2 for exit:\n ")
    run = True if inp == "1" else False

# cd.Coding()
# cd.Coding()
# cd.Decoding()
# cd.Decoding()

# word="Have a good day"
# print(word[::-1]) #This technique involve reversing the string.
# print(word[-1] +word[:-1]) #In this technique we add first letter in the end.