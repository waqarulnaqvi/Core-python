class Remote():
    pass

class Player:#Encapsulation rapping up it into a capsule like you rap (the Player all the function into the player class) like an capsule..
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

    def moveBottom(self):
        pass   

remote1= Remote()
player1=Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()
# abstractin me layer of details chuppa li jaati hai user se..like aapke phone ka button (layer of abstraction) ka part hai..


