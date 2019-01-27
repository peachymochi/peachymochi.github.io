"""
Hello, welcome to my snake game. In order to be able to run and play this game, you must have pygame.
If you do not have pygame, you can go to: https://www.pygame.org/wiki/GettingStarted
and install the program.

"""
import pygame
import time
import random

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

#1.) I added background music to the game by using this video to help me: https://www.youtube.com/watch?v=YQ1mixa9RAw
#BGM
pygame.mixer.music.load("C:/Users/eun/Desktop/Paper Mario Music - Shy Guy's Toy Box.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (109,235,255)
gray = (227,242,244)

#display size
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

#game name/window title 
pygame.display.set_caption("Snakey")

icon = pygame.image.load("C:/Users/eun/Desktop/apple.png")
pygame.display.set_icon(icon)

#images
img = pygame.image.load("C:/Users/eun/Desktop/snakeHead.png")
appleimg = pygame.image.load("C:/Users/eun/Desktop/apple.png")
bappleimg = pygame.image.load("C:/Users/eun/Desktop/bapple.png")


clock = pygame.time.Clock()

#apple size/black apple size("Bapple")/block size/FPS value
Bapple_Thickness = 30
AppleThickness = 30
block_size = 20
FPS = 30

direction = "right"


#2.) I changed the font and font size by using the information given from the tutorial.
#font
smallfont = pygame.font.SysFont("couriernew",20)
medfont = pygame.font.SysFont("couriernew",25)
largefont = pygame.font.SysFont("ocraextended",70)

def pause():

    paused = True
    
    message_to_screen("Paused", black, -100, size = "large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)
    

def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY

#3.) I added another apple, but if the snake eats the black apple it dies. I based it off on the information from the tutorial when making the apple and the code for the rest/most of it is near the bottom of def gameLoop().
def randBappleGen():
    randBappleX = round(random.randrange(0,display_width-Bapple_Thickness))#/10.0)*10.0
    randBappleY = round(random.randrange(0,display_height-Bapple_Thickness))#/10.0)*10.0

    return randBappleX,randBappleY


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
#4.) I changed the display color from white to light gray as well as adding a message in the intro by using the information given in the tutorial and RGB color picker.    
        gameDisplay.fill(gray)
        message_to_screen("Welcome to Snakey!", blue, -100,"large")
        message_to_screen("The objective of the game is to eat red apples.", black, -30)
        message_to_screen("The more apples you eat, the longer you get.", black, 10)
        message_to_screen("If you run into yourself, or the edges, you die.", black, 50)
        message_to_screen("Avoid eating the black apples or you die.", black, 90)
        message_to_screen("Press C to play, P to pause, or Q to quit.", black, 180)

        pygame.display.update()
        clock.tick(15)


#snake drawing
def snake(block_size,snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img,270)

    if direction == "left":
        head = pygame.transform.rotate(img,90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img,180)
        
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))

#5.) I changed the color of the snake from green to blue by using the information given in the tutorial and RGB color picker.
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,blue,[XnY[0],XnY[1],block_size,block_size])


def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)

    elif size == "medium":
        textSurface = medfont.render(text,True,color)

    elif size == "large":
        textSurface = largefont.render(text,True,color)
        
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color,y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)


def gameLoop():
    global direction

    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
    randAppleX,randAppleY = randAppleGen()
    randBappleX,randBappleY = randBappleGen()
    
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over",red,y_displace=-50, size = "large")
            message_to_screen("Press C to play again or Q to quit",black,50, size = "medium")
            pygame.display.update()
            

        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        
                    if event.key == pygame.K_c:
                        gameLoop()


            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                    
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                    
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            

        lead_x += lead_x_change
        lead_y += lead_y_change

        
        #background color
        gameDisplay.fill(gray)
        
        #apple drawing
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        #bapple drawing
        gameDisplay.blit(bappleimg, (randBappleX, randBappleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True 
            
        snake(block_size,snakeList)

        score(snakeLength-1)
        
        pygame.display.update()
        
        
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                    randAppleX,randAppleY = randAppleGen()
                    snakeLength += 1
                    
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                    randAppleX,randAppleY = randAppleGen()
                    snakeLength += 1

        if lead_x > randBappleX and lead_x < randBappleX + Bapple_Thickness or lead_x + block_size > randBappleX and lead_x + block_size < randBappleX + Bapple_Thickness:
            if lead_y > randBappleY and lead_y < randBappleY + Bapple_Thickness:
                    randBappleX,randBappleY = randBappleGen()
                    clock.tick(0)
                    gameOver = True
                    
            elif lead_y + block_size > randBappleY and lead_y + block_size < randBappleY + Bapple_Thickness:
                    randBappleX,randBappleY = randBappleGen()
                    clock.tick(0)
                    gameOver = True
                    

            
        clock.tick(FPS)

        
    #quit everything  
    pygame.quit()
    quit()

game_intro()
gameLoop()
