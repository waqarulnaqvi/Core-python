# Exercise :5
"""
                S W G
computer =     -1 0 1
player   =S -1  D W L
          W  0  L D W
          G  1  W L D
"""
# 16 54
import random

class swg:
    def __init__(self):
        self.countc=0
        self.countp=0

    randum=lambda self :random.randint(-1,1)

    # @staticmethod
    # def randnum(self):
    #     a=random.randint(-1,1)
    #     return a

    # def infloop(self,func ):
    #     def mfunc(*args,**kwargs):
    #         print("Hello World")
    # #         while True:
    # #             print("wewewe")
    #         func(self,*args,**kwargs)
    #         print("Yellow world")
    #     return mfunc

    # @infloop
    # def ret(self):
    #     print("Wowwwww!!!!!!")

    # @infloop
    def loop(self):
      while True:
        b = self.randum()
        inp = int(input("""
Enter -1 for snake S
Enter  0 for Water W
Enter  1 for Gun   G
Press any key to exit:
"""))
        # 13 8

        match (inp):
            case 0:
                print("YOU CHOOSE WATER")
                # a=self.randnum(self)
                # print(a)
                # print(b)
                if b==inp:
                    print("DRAW")
                    print("Computer choose Water")
                elif b+inp==-1:
                    print("YOU LOSE COMPUTER WIN!!")
                    print("Computer choose Snake")
                    # self.countc+=1
                    self.countp-=1
                else:
                    print("Computer choose Gun")
                    print("YOU WIN COMPUTER LOSE!!")
                    # self.countc-=1
                    self.countp+=1

            case 1:
                print("YOU CHOOSE GUN")
                if b == inp:
                    print("COMPUTER CHOOSE GUN")
                    print("DRAW")

                elif b + inp == 0:
                    print("YOU WIN COMPUTER LOSE!!")
                    print("Computer choose Snake")
                    # self.countc -= 1
                    self.countp += 1
                else:
                    print("YOU LOSE COMPUTER WIN!!")
                    print("Computer choose Water")
                    # self.countc += 1
                    self.countp -= 1

            case -1:
                print("YOU CHOOSE SNAKE")
                if b == inp:
                    print("DRAW")
                    print("Computer choose Snake")
                elif b + inp == -1:
                    print("YOU WIN COMPUTER LOSE!!")
                    print("COMPUTER CHOOSE GUN")
                    # self.countc -= 1
                    self.countp += 1
                else:
                    print("YOU LOSE COMPUTER WIN!!")
                    print("Computer choose Water")
                    # self.countc += 1
                    self.countp -= 1

            case _:
                # print(f"""
                #     Results:
                #     Player : {self.countp}
                #     Computer :{self.countc}""")
                if self.countp>0:
                     print("You won")
                     print("Computer lose")
                     print(self.countp)
                elif self.countp<0:
                    print("Computer won")
                    print("You lose")
                    print(self.countp)
                else:
                    print("DRAW!!")
                print("GAME OVER!!")
                exit()

ob=swg()
# ob.ret()
# ob.infiniteloop(ob.loop())
ob.loop()
# 23 50
