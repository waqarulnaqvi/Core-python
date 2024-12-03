import random,string
class Coding_Decoding:
    def __init__(self,str):
        self.str=str
        self.layer=self.decode=0

    def Coding(self):
        self.starting_rand_alp="".join(random.choices(string.ascii_letters,k=3))
        self.ending_rand_alp="".join(random.sample(string.ascii_letters,3))
        self.strr=""
        self.layer+=1
        strlist=self.str.split(" ")
        for word in strlist:
            if  len(word) < 3:
                 self.strr+=word[: :-1]+" "
            else:
                self.strr+=self.starting_rand_alp+word[1:]+word[0]+self.ending_rand_alp+" "
        print(f"Original Message is : {self.str}")
        print(f"{self.layer} layer Encoded Message:")
        print(self.strr,end="\n\n")
        self.str=self.strr

    def Decoding(self):
        decodedstr = self.str.split(" ")
        self.strr = ""
        for word in decodedstr:
            if len(word) >= 3 and len(word) <= 8:
                print("The Message is already in Decoded format!!")
                self.strr=0
                break
            elif len(word) < 3:
                self.strr += word[::-1] + " "
            else:
                self.strr += word[-4] + word[3:-4] + " "
        if self.layer!=0:
            self.layer -= 1
        if  self.strr !=0 :
           self.decode += 1
           self.str=self.strr
        print(f"Total Decoding operation performed {self.decode}\nThe Decoded Message is:")
        print(self.str,end="\n\n")

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

# 12 32
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