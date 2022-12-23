import pygame
# 8-arrays instead of 1 4-by-4 array

# array representation of 4-by-4 grid
arr_repr = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

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
    high_score = pygame.Rect(770, 410, 200, 175)
    pygame.draw.rect(screen, (200, 200, 200), high_score, border_radius=20)
    pygame.draw.lines(screen, (250,250,250), True, [(770,465), (970,465)])


    # replicate arr_repr into the 4-by-4 grid
    for i in range(0, 4):
        for j in range(0, 4):
            if arr_repr[i][j] == 0:
                pass
            elif arr_repr[i][j] == 2:
                pass
            elif arr_repr[i][j] == 4:
                pass
            elif arr_repr[i][j] == 8:
                pass
            elif arr_repr[i][j] == 16:
                pass
            elif arr_repr[i][j] == 32:
                pass
            elif arr_repr[i][j] == 64:
                pass
            elif arr_repr[i][j] == 128:
                pass
            elif arr_repr[i][j] == 256:
                pass
            elif arr_repr[i][j] == 512:
                pass
            elif arr_repr[i][j] == 1024:
                pass
            elif arr_repr[i][j] == 2048:
                pass

    pygame.display.flip()

pygame.quit()




