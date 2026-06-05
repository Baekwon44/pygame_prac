import pygame as py
import sys
width=800
height=400

screen = py.display.set_mode((width,height))

clock=py.time.Clock()
rect_x=200
rect_y=100
rect_speed=5
running=True
while running:
    clock.tick(60)
    for event in py.event.get():
        if event.type==py.QUIT:
            running=False
    screen.fill((255,70,162))
    keys=py.key.get_pressed()

    if keys[py.K_a]:
        rect_x -= rect_speed
    if keys[py.K_d]:
        rect_x += rect_speed
    if keys[py.K_w]:
        rect_y -= rect_speed
    if keys[py.K_s]:
        rect_y += rect_speed

    rect = py.Rect(rect_x, rect_y, 50, 50)
    py.draw. rect(screen, (255,0,0), rect)
    py.display.flip()




py.quit()
sys.exit()
py.init()