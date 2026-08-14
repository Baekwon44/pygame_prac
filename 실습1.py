import pygame as py
import sys
py.init()
clock=py.time.Clock()

Width, Height = 600,600
Line_Width = 15
White = (255,255,255)
Line_color = (0,0,0)

screen = py.display.set_mode((Width, Height))
py.display.set_caption('tic-tak-toe')

def draw_line():
    screen.fill(White)
    py.draw.line(screen, Line_color, (0, Height//3), (Width, Height//3), Line_Width)
    py.draw.line(screen, Line_color, (0, 2*Height//3), (Width, 2*Height//3), Line_Width)

    py.draw.line(screen, Line_color, (Width//3, 0), (Width//3, Height), Line_Width)
    py.draw.line(screen, Line_color, (2*Width//3, 0), (2*Height//3, Height), Line_Width)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    draw_line()

    py.display.flip()
    clock.tick(60)

py.quit()
sys.exit()