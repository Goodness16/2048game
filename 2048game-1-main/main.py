import pygame
import functions
# 8-arrays instead of 1 4-by-4 array

# array representation of 4-by-4 grid
arr_repr = [[2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2]]
curr_score_value = 0

# left and up borders for all the squares on the 4-by-4 grid
loc = {'00':[50,50], '01':[225,50], '02':[400,50], '03':[575,50],
       '10':[50,225], '11':[225,225], '12':[400,225], '13':[575,225],
       '20':[50,400], '21':[225,400], '22':[400,400], '23':[575,400],
       '30':[50,575], '31':[225,575], '32':[400,575], '33':[575,575]}


pygame.init()

# define screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# game loop
running = True
while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changed, score = functions.left(arr_repr)
                curr_score_value += score
                if changed:
                    functions.random_insert(arr_repr)
                break
            elif event.key == pygame.K_RIGHT:
                changed, score = functions.right(arr_repr)
                curr_score_value += score
                if changed:
                    functions.random_insert(arr_repr)
                break
            elif event.key == pygame.K_UP:
                changed, score = functions.up(arr_repr)
                curr_score_value += score
                if changed:
                    functions.random_insert(arr_repr)
                break
            elif event.key == pygame.K_DOWN:
                changed, score = functions.down(arr_repr)
                curr_score_value += score
                if changed:
                    functions.random_insert(arr_repr)
                break
    # background
    screen.fill((250, 250, 250))

    # draw a square board
    board = pygame.Rect(50, 50, 700, 700)
    pygame.draw.rect(screen, (200, 200, 200), board, border_radius=10)

    # draw vertical lines
    pygame.draw.lines(screen, (250,250,250), True, [(225,50), (225,750)], 5)
    pygame.draw.lines(screen, (250,250,250), True, [(400,50), (400,750)], 5)
    pygame.draw.lines(screen, (250,250,250), True, [(575,50), (575,750)], 5)

    # draw horizontal lines
    pygame.draw.lines(screen, (250,250,250), True, [(50,225), (750,225)], 5)
    pygame.draw.lines(screen, (250,250,250), True, [(50,400), (750,400)], 5)
    pygame.draw.lines(screen, (250,250,250), True, [(50,575), (750,575)], 5)

    # draw a current score and high score box
    curr_score = pygame.Rect(770, 215, 200, 175)
    pygame.draw.rect(screen, (200, 200, 200), curr_score, border_radius=20)
    pygame.draw.lines(screen, (250,250,250), True, [(770,270), (970,270)])
    font = pygame.font.SysFont(None, 60)
    img = font.render("SCORE", True, (0, 0, 0))
    screen.blit(img, (795, 225))
    if len(str(curr_score_value)) == 1:
        font = pygame.font.SysFont(None, 100)
        img = font.render(str(curr_score_value), True, (0, 0, 0))
        screen.blit(img, (850, 300))
    if len(str(curr_score_value)) == 2:
        font = pygame.font.SysFont(None, 100)
        img = font.render(str(curr_score_value), True, (0, 0, 0))
        screen.blit(img, (825, 300))
    if len(str(curr_score_value)) == 3:
        font = pygame.font.SysFont(None, 100)
        img = font.render(str(curr_score_value), True, (0, 0, 0))
        screen.blit(img, (810, 300))
    if len(str(curr_score_value)) == 4:
        font = pygame.font.SysFont(None, 90)
        img = font.render(str(curr_score_value), True, (0, 0, 0))
        screen.blit(img, (800, 300))
    if len(str(curr_score_value)) == 5:
        font = pygame.font.SysFont(None, 80)
        img = font.render(str(curr_score_value), True, (0, 0, 0))
        screen.blit(img, (785, 300))
    high_score = pygame.Rect(770, 410, 200, 175)
    pygame.draw.rect(screen, (200, 200, 200), high_score, border_radius=20)
    pygame.draw.lines(screen, (250,250,250), True, [(770,465), (970,465)])


    # replicate arr_repr into the 4-by-4 grid
    for i in range(0, 4):
        for j in range(0, 4):
            if arr_repr[i][j] == 0:
                # key = str(i) + str(j)
                # left, up = loc[key]
                # tile = pygame.Rect(left+10, up+10, 16, 165)
                # pygame.draw.rect(screen, (200, 200, 200), tile)
                pass

            elif arr_repr[i][j] == 2:
                # Creating the number tiles

                key=str(i)+str(j)
                left,up=loc[key]
                tile= pygame.Rect(left+7, up+7, 160, 160)
                pygame.draw.rect(screen, (156,175,183), tile, border_radius=20)
                font = pygame.font.SysFont(None, 180)
                img = font.render('2', True, (255,255,255))
                screen.blit(img, (left+50, up+30))
            elif arr_repr[i][j] == 4:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (241,174,104), tile, border_radius=20)
                font = pygame.font.SysFont(None, 180)
                img = font.render('4', True, (255, 255, 255))
                screen.blit(img, (left + 50, up + 30))
            elif arr_repr[i][j] == 8:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (244,204,204), tile, border_radius=20)
                font = pygame.font.SysFont(None, 180)
                img = font.render('8', True, (255, 255, 255))
                screen.blit(img, (left + 50, up + 30))
            elif arr_repr[i][j] == 16:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (147,196,125), tile, border_radius=20)
                font = pygame.font.SysFont(None, 160)
                img = font.render('16', True, (255, 255, 255))
                screen.blit(img, (left + 20, up + 40))
            elif arr_repr[i][j] == 32:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (174,167,167), tile, border_radius=20)
                font = pygame.font.SysFont(None, 160)
                img = font.render('32', True, (255, 255, 255))
                screen.blit(img, (left + 20, up + 40))
            elif arr_repr[i][j] == 64:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (114,91,209), tile, border_radius=20)
                font = pygame.font.SysFont(None, 160)
                img = font.render('64', True, (255, 255, 255))
                screen.blit(img, (left + 30, up + 40))
            elif arr_repr[i][j] == 128:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (199,196,85), tile, border_radius=20)
                font = pygame.font.SysFont(None, 130)
                img = font.render('128', True, (255, 255, 255))
                screen.blit(img, (left +10 , up + 50))
            elif arr_repr[i][j] == 256:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (115,115,115), tile, border_radius=20)
                font = pygame.font.SysFont(None, 130)
                img = font.render('256', True, (255, 255, 255))
                screen.blit(img, (left + 15, up + 50))
            elif arr_repr[i][j] == 512:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (247,80,80), tile, border_radius=20)
                font = pygame.font.SysFont(None, 130)
                img = font.render('512', True, (255, 255, 255))
                screen.blit(img, (left + 10, up + 50))
            elif arr_repr[i][j] == 1024:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (143,206,0), tile, border_radius=20)
                font = pygame.font.SysFont(None, 100)
                img = font.render('1024', True, (255, 255, 255))
                screen.blit(img, (left +10 , up + 55))
            elif arr_repr[i][j] == 2048:
                # Creating the number tiles

                key = str(i) + str(j)
                left, up = loc[key]
                tile = pygame.Rect(left + 7, up + 7, 160, 160)
                pygame.draw.rect(screen, (247,219,167), tile, border_radius=20)
                font = pygame.font.SysFont(None, 95)
                img = font.render('2048', True, (255, 255, 255))
                screen.blit(img, (left + 10, up + 55))

    pygame.display.flip()

pygame.quit()
