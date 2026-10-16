import pygame as py
import sys
import random as rd
py.init()

Width,Height = 600, 700
Top = 100
Cell = 200
Mole_interval = 600
Game_time = 30

Grass_color = (120, 200, 90)
Hole_color = (60, 40, 20)
Board_color = (255,255,255)
Mole_color = (140,90,50)
Eye_color = (0,0,0)
Nose_color = (240,120,140)
Text_color = (0,0,0)

screen = py.display.set_mode((Width, Height))
py.display.set_caption('두더지 잡기')

clock = py.time.Clock()
font = py.font.SysFont(None,50)

mole_row = rd.randint(0,2)
mole_col = rd.randint(0,2)
last_move_time = py.time.get_ticks()
score = 0
start_time = py.time.get_ticks()
game_over = False


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

def move_mole():
    global mole_row, mole_col, last_move_time
    new_row = mole_row
    new_col = mole_col
    while new_row == mole_row and new_col == mole_col:
        new_row = rd.randint(0,2)
        new_col = rd.randint(0,2)
    mole_row = new_row
    mole_col = new_col
    last_move_time = py.time.get_ticks()


def draw_statue(remaining):
    score_surface = font.render(f"Score : {score}", True, Text_color)
    screen.blit(score_surface, (30,30))
    time_surface = font.render(f"Time : {remaining}", True, Text_color)
    screen.blit(time_surface, (Width - 180,30))

def draw_game_over():
    lines = [f"Game over! Score : {score}", "Press 'R' to Restart"]
    for i in range(len(lines)):
        text_surface = font.render(lines[i], True, Text_color)
        text_rect = text_surface.get_rect(center=(Width // 2, Height // 2 + i * 60))
        py.draw.rect(screen, Board_color, text_rect.inflate(20,10))
        screen.blit(text_surface, text_rect)

def restart():
    global score, start_time, game_over
    score = 0
    start_time = py.time.get_ticks()
    game_over = False
    move_mole()


running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            if mouseY >= Top:
                clicked_row = (mouseY - Top) // Cell
                clicked_col = mouseX // Cell

                if clicked_row == mole_row and clicked_col == mole_col:
                    score += 1
                    move_mole()
                    now = py.time.get_ticks()

                    if now - last_move_time >= Mole_interval:
                        move_mole()

        if event.type == py.KEYDOWN:
            if event.key == py.K_r:
                restart()
    
    now = py.time.get_ticks()

    remaining = Game_time - (now - start_time) // 1000
    if remaining <= 0:
        remaining = 0
        game_over = True

    if not game_over and now - last_move_time >= Mole_interval:
        move_mole()

    if now - last_move_time >= Mole_interval:
        move_mole()

    draw_board()
    if game_over:
        draw_game_over()
    else:
        draw_mole()
    draw_mole()
    draw_statue(remaining)

    py.display.flip()
    clock.tick(60)

py.quit()
sys.exit()
