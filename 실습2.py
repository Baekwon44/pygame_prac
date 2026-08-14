import pygame as py
import sys
py.init()
clock=py.time.Clock()

Width, Height = 600,600
Line_Width = 15
Circle_radius = 60
Circle_width = 15
Cross_width = 25
space = 55

White = (255,255,255)
Line_color = (0,0,0)
Circle_color = (242, 85, 96)
Cross_color = (28, 170, 156)

screen = py.display.set_mode((Width, Height))
py.display.set_caption('tic-tak-toe')

board = [
    [1, 0, 2],
    [0, 1, 0],
    [2, 0, 1]
]

def draw_line():
    screen.fill(White)
    py.draw.line(screen, Line_color, (0, Height//3), (Width, Height//3), Line_Width)
    py.draw.line(screen, Line_color, (0, 2*Height//3), (Width, 2*Height//3), Line_Width)

    py.draw.line(screen, Line_color, (Width//3, 0), (Width//3, Height), Line_Width)
    py.draw.line(screen, Line_color, (2*Width//3, 0), (2*Height//3, Height), Line_Width)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:

                center_x = col * (Width // 3) + (Width // 6)
                center_y= row * (Height // 3) + (Height // 6)
                py.draw.circle(screen,Circle_color, (center_x, center_y), Circle_radius, Circle_width)

            elif board[row][col] == 2:
                start_x = col * (Width // 3) + space
                start_y= row * (Height // 3) + space
                end_x = (col + 1) * (Width // 3) - space
                end_y = (row + 1) * (Height // 3) - space

                py.draw.line(screen, Cross_color, (start_x, end_y), (end_x, start_y), Cross_width)
                py.draw.line(screen, Cross_color, (start_x, start_y), (end_x, end_y), Cross_width)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    draw_line()
    draw_figures()

    py.display.flip()
    clock.tick(60)

py.quit()
sys.exit()