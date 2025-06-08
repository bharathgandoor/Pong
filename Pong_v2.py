import random                       ##Import Random                             
import pygame                       ##Pygame basecode.
pygame.init()
screen=pygame.display.set_mode((640,640))                                  
pygame.display.set_caption("Pong, but it's coded with classes.")

class ball:                                                        ##The ball.
    def __init__(self, size, x_speed, y_speed, x, y):
        self.size = size
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x = x
        self.y = y

class paddle:                                                      ##The paddle.
    def __init__(self, start_x, start_y, x_size, y_size, y_speed):
        self.start_x = start_x
        self.start_y = start_y
        self.x_size = x_size
        self.y_size = y_size
        self.y_speed = y_speed

theball = ball(7,0,0,320,320)                 ##Set parameters for the ball.

paddle_L = paddle(15, 290, 10, 60, 5)         ##Set parameters for the paddles.
paddle_R = paddle(610, 290, 10, 60, 5)

StartVar = False
WhichDirection = [-3,3]

L_Down = False
R_Down = False
L_Up = False
R_Up = False

def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans",24)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
ScoreLeft = 0
ScoreRight = 0

while True:                                                                                                      ##Display everything.
    screen.fill((0,0,0))
    show_text("Left team score: " + str(ScoreLeft), 20, 20, (0,0,255))
    show_text("Right team score: " + str(ScoreRight), 400, 20, (255,0,0))
    leftpaddle = pygame.draw.rect(screen,(0,0,255),(paddle_L.start_x, paddle_L.start_y, paddle_L.x_size, paddle_L.y_size))    ##Left Paddle
    if L_Down == True:
        paddle_L.start_y+=paddle_L.y_speed
    if L_Up == True:
        paddle_L.start_y-=paddle_L.y_speed
    rightpaddle = pygame.draw.rect(screen,(255,0,0),(paddle_R.start_x, paddle_R.start_y, paddle_R.x_size, paddle_R.y_size))    ##Right Paddle.
    if R_Down == True:
        paddle_R.start_y+=paddle_R.y_speed
    if R_Up == True:
        paddle_R.start_y-=paddle_R.y_speed
    greenball = pygame.draw.circle(screen,(0,255,0),(theball.x, theball.y), theball.size)                                    ##The ball.
    if theball.x >= 640:                                                                                                     ##Score for the left.
        ScoreLeft+=1
        theball.x = 320
        theball.y = 320
        theball.y_speed = 0
        theball.x_speed = 0
    if theball.x <= 0:                                                                                                     ##Score for the left.
        ScoreRight+=1
        theball.x = 320
        theball.y = 320
        theball.y_speed = 0
        theball.x_speed = 0
    if theball.y >= 640 or theball.y <=0:                                                                                   ##Make contact with roof or floor.
        theball.y_speed = -theball.y_speed
    if leftpaddle.colliderect(greenball) == True:                                                                           ##Ball collides with left paddle.
        theball.x_speed = -theball.x_speed
        theball.y_speed = random.randint(-7,7)
    if rightpaddle.colliderect(greenball) == True:                                                                          ##Ball collides with right paddle.
        theball.x_speed = -theball.x_speed
        theball.y_speed = random.randint(-7,7)
    theball.x+=theball.x_speed
    theball.y+=theball.y_speed
    pygame.display.update()
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                theball.x_speed = random.choice(WhichDirection)
                theball.x = 320
                theball.y = 320
                                                                                                                        ##Paddle movement keys pressed down.
            if event.key == pygame.K_l:
                R_Down = True
            if event.key == pygame.K_o:                                                         
                R_Up = True
            if event.key == pygame.K_w:
                L_Up = True
            if event.key == pygame.K_s:
                L_Down = True
                                                                                                                        ##Paddle movement keys released.     
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                R_Down = False
            if event.key == pygame.K_o:
                R_Up = False
            if event.key == pygame.K_w:
                L_Up = False
            if event.key == pygame.K_s:
                L_Down = False
                
        if event.type == pygame.QUIT:                                                                                   ##Quit Pygame.
            pygame.quit()
            exit()
