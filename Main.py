import random
import pygame
a = pygame.init()

screen_hight = 500
screen_width = 350

window = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Snake Game")
pygame.display.update()

font = pygame.font.SysFont(None, 25)
font_1 = pygame.font.SysFont(None, 30)

exit = False
over = False 
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])

def text_screen1(text, color, x, y):
    screen_text = font_1.render(text, True, color)
    window.blit(screen_text, [x, y])

def snake_plot(window, color, snk_list, var_size):
    for x,y in snk_list:
        pygame.draw.rect(window, color, [x, y, var_size, var_size] )

def welcome():
    exit = False
    while not exit:
        window.fill(white)
        text_screen1("Welcome to Snakes", black, 85, 200)
        text_screen1("Press Space bar to play", black, 65, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
            
        pygame.display.update()
        clock.tick(30)

def gameloop():

    var_x = 45
    var_y = 55
    var_size = 20
    # var_food = 20
    vel_x = 0
    vel_y = 0 
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_hight/2)
    Score = 0
    fps = 30
    exit = False
    over = False 
  
    with open("highscore.txt", "r") as h:
        highscore = h.read()
    snk_list = []
    snk_length = 1
    while not exit:
        if over:
            with open("highscore.txt", "w") as h:
                h.write(str(highscore))
            window.fill(white)
            text_screen("Game Over! Press Enter to continue.", red , screen_width/10, screen_hight/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == 1073741912:
                        gameloop()

        else:    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = 7
                        vel_y = 0
                    if event.type == pygame.QUIT:
                        exit = True
                    if event.key == pygame.K_LEFT:
                        vel_x = -7
                        vel_y = 0
                    if event.key == pygame.K_UP:
                        vel_y = -7
                        vel_x = 0
                    if event.key == pygame.K_DOWN:
                        vel_y = 7
                        vel_x = 0
                    if event.key == pygame.K_q:
                    # cheat code
                    # press "q" to increase your score by 10 
                        Score += 10
                        

            window.fill(white)
            text_screen("Score is: "+ str(Score) + "  High-score is: " +str(highscore), red, 5, 5)
            snake_plot(window, black, snk_list, var_size)
            pygame.draw.rect(window, red, [food_x, food_y, var_size, var_size] )

            var_x = var_x + vel_x
            var_y = var_y + vel_y
            if abs(var_x - food_x)<10 and abs(var_y - food_y)<10:
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_hight/2)
                Score += 1
                snk_length += 3
                if Score>int(highscore):
                    highscore = Score

            if var_x<0 or var_x>screen_width or var_y<0 or var_y>screen_hight:
                over = True
            head = []
            head.append(var_x)
            head.append(var_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                over = True        
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()
welcome()