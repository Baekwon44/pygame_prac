import pygame as py
import sys
import random as rd
py.init()

Width,Height = 600, 700
Top = 100
Cell = 200

Grass_color = (120, 200, 90)
Hole_color = (60, 40, 20)
Board_color = (255,255,255)
Mole_color = (140,90,50)
Eye_color = (0,0,0)
Nose_color = (240,120,140)

screen = py.display.set_mode((Width, Height))
py.display.set_caption('두더지 잡기')

clock = py.time.Clock()

mole_row = rd.randint(0,2)
mole_col = rd.randint(0,2)


def cell_center(row, col):
    center_x = col * Cell + Cell // 2
    center_y = Top + row * Cell + Cell // 2
    return center_x, center_y

def draw_board():
    screen.fill(Grass_color)
    py.draw.rect(screen, Board_color, (0,0,Width,Top))
    for row in range(3):
        for col in range(3):
            center_x,center_y = cell_center(row,col)
            py.draw.ellipse(screen,Hole_color, (center_x - 70, center_y + 10,140,50))
def draw_mole() :
    center_x, center_y = cell_center(mole_row,mole_col)
    py.draw.circle(screen, Mole_color, (center_x, center_y), 50)
    py.draw.circle(screen, Eye_color, (center_x - 18, center_y - 12), 6)
    py.draw.circle(screen, Eye_color, (center_x + 18, center_y - 12), 6)
    py.draw.circle(screen, Nose_color, (center_x, center_y + 8), 9)


running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    draw_board()
    draw_mole()

    py.display.flip()
    clock.tick(60)

py.quit()
sys.exit()
