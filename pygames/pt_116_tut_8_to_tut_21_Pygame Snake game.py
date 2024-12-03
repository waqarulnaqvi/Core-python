import pygame
import random
import os
pygame.mixer.init()
pygame.init()

# pygame.mixer.music.stop()
# Everygame is a computer program which is stored in a memory

# Colors
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
# Creating window
gameWindow=pygame.display.set_mode((800,500))
# Defining screen width and height
screen_width=900
screen_height=600

# Game title
pygame.display.set_caption("Snakes With mysteriouscoder__")
pygame.display.update()#to implement changes we have to update the  pygame.display

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def image(img):
    bgimg=pygame.image.load(img)
    bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
    return bgimg
#     Because of convert alpha game speed does not affected by img
def music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size,snake_size])
        # It is the most simplest way to draw rectangle with the help of pygames

# Game Loop

def updating_high_score():
    # Check if highscore file exist:
    if (not os.path.exists("pt_116_high score.txt")):
        with open("pt_116_high score.txt","w") as f:
           f.write("0")
    with open("pt_116_high score.txt", "r") as f:
        return f.read()


def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(image("game_background_image.jpg"),(0,0))
        text_screen("Welcome to Snakes",black,180,170)
        text_screen("Press Space Bar to play",black,180,220)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    music('game start.mp3')
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    # Random module generate integer on the basis of screen width and screen height
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 50
    snake_size = 10
    fps = 60
    init_velocity = 2
    score = velocity_x = 0
    foodlength=1
    velocity_y = 0
    snk_list = []
    snk_lenght = 5
    while not exit_game:
        highscore=updating_high_score()
        if score > int(highscore):
            with open('pt_116_high score.txt',"w") as f:
                highscore = str(score)
                f.write(highscore)

        if  game_over:
            gameWindow.fill(white)
            gameWindow.blit(image("game_background_image.jpg"), (0, 0))
            text_screen(f"Game Over!!",red,180,170)
            text_screen(f"Your Score :{score}",green,180,220)

            text_screen(f"High Score :{highscore}",green,180,270)
            text_screen(f"Press Enter to Continue",black,180,320)


            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                        snake_x=snake_x+10
                        velocity_x = init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                        snake_x=snake_x-10
                        velocity_x = -init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP or event.key==pygame.K_w:
                        snake_y=snake_y-10
                        velocity_x =0
                        velocity_y=-init_velocity
                    if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                        snake_y=snake_y+10
                        velocity_x =0
                        velocity_y=init_velocity
                    if event.key==pygame.K_f:
                        score+=10
                    if event.key==pygame.K_l:
                        snk_lenght+=5
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            gameWindow.fill(green)
            text_screen(f"Score : {str(score)}  High Score : {highscore}" ,blue,5,5)
            if foodlength%5==0:
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size + 14, snake_size + 14])
                if abs(snake_x - food_x) < 21 and abs(snake_y - food_y) < 21:
                    music('bigfood.mp3')
                    score += 30
                    init_velocity += 0.25
                    # print("Score :"+str(score*10))
                    food_x = random.randint(20, screen_width // 2)
                    food_y = random.randint(20, screen_height // 2)
                    snk_lenght += 5
                    foodlength+=1
            else:
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size , snake_size ])
                if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
                    music('food.mp3')
                    score+=10
                    init_velocity+=0.25
                    food_x=random.randint(20,screen_width//2)
                    food_y=random.randint(20,screen_height//2)
                    snk_lenght+=5
                    foodlength+=1

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_lenght:
                del snk_list[0]
            if head in snk_list[4:-1]:
                music('gameover.mp3')
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                music('gameover.mp3')
                game_over=True
            pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size+5,snake_size+5])#It is the most simplest way to draw rectangle with the help of pygames
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()#to implement changes we have to update the  pygame.display

        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
