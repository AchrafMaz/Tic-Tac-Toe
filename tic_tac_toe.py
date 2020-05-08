import pygame
import numpy as np
WIDTH = 600
HEIGHT = 600
WHITE = (255,255,255)
win = pygame.display.set_mode((WIDTH,HEIGHT))
win.fill((0,0,200))
table = np.zeros((3,3))
run = True

def draw(x,y):
    pygame.draw.line(win,WHITE,x,y,7)
def draw_x(x,y):
    pygame.draw.line(win,(200,0,0),(x,y),(x+200,y+200),4)
    pygame.draw.line(win,(200,0,0),(x+200,y),(x,y+200),4)

def draw_o(x,y):
    pygame.draw.circle(win,(200,0,0),(x,y),90,3)

def move_o():

    t  =pygame.mouse.get_pos()
    if t[0] < 200:
        if t[1] < 200 :
            draw_o(100,100)
            table[0,0]=1
        if t[1] > 200 and t[1] < 400 :
            draw_o(100,300)
            table[1,0]=1
        if t[1] > 400 and t[1] < 600:
            draw_o(100,500)
            table[2,0]=1
    if t[0] < 400 and t[0] > 200:
        if t[1] < 200 :
            draw_o(300,100)
            table[0, 1] = 1
        if t[1] > 200 and t[1] < 400 :
            draw_o(300,300)
            table[1, 1] = 1
        if t[1] > 400 and t[1] < 600:
            draw_o(300,500)
            table[2, 1] = 1
    if t[0] < 600 and t[0] > 400:
        if t[1] < 200 :
            draw_o(500,100)
            table[0, 2] = 1
        if t[1] > 200 and t[1] < 400 :
            draw_o(500,300)
            table[1, 2] = 1
        if t[1] > 400 and t[1] < 600:
            draw_o(500,500)
            table[2, 2] = 1
    print(table)


def move_x():
    t  =pygame.mouse.get_pos()
    if t[0] < 200:
        if t[1] < 200 :
            draw_x(0,0)
            table[0, 0] = 2
        if t[1] > 200 and t[1] < 400 :
            draw_x(0,200)
            table[1, 0] = 2
        if t[1] > 400 and t[1] < 600:
            draw_x(0,400)
            table[2, 0] = 2
    if t[0] < 400 and t[0] > 200:
        if t[1] < 200 :
            draw_x(200,00)
            table[0, 1] = 2
        if t[1] > 200 and t[1] < 400 :
            table[1, 1] = 2
            draw_x(200,200)
        if t[1] > 400 and t[1] < 600:
            draw_x(200,400)
            table[2, 1] = 2
    if t[0] < 600 and t[0] > 400:
        if t[1] < 200 :
            draw_x(400,00)
            table[0, 2] = 2
        if t[1] > 200 and t[1] < 400 :
            table[1, 2] = 2
            draw_x(400,200)
        if t[1] > 400 and t[1] < 600:
            draw_x(400,400)
            table[2, 2] = 2
    print(table)
draw((200,0),(200,600))
draw((400,0),(400,600))
draw((0,200),(600,200))
draw((0,400),(600,400))
pygame.display.flip()
player = 1
player1 = 2
board = table

r = 0
while run:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if r==1:
                move_x()
                r = 0
            else:
                move_o()
                r=1

        pygame.display.flip()

    if any([(board[0, :] == player).all(),
            (board[:, 0] == player).all(),
            (board[1, :] == player).all(),
            (board[:, 1] == player).all(),
            (board[2, :] == player).all(),
            (board[:, 2] == player).all()]):
        run = False
        print(" O win")
    if any([(board[0, :] == player1).all(),
            (board[:, 0] == player1).all(),
            (board[1, :] == player1).all(),
            (board[:, 1] == player1).all(),
            (board[2, :] == player1).all(),
            (board[:, 2] == player1).all()]):
        run = False
        print("X win")
