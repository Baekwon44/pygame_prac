import pygame as py
import sys

py.init()

WIDTH=800
HEIGHT=600

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("충돌 감지 예제")
clock = py.time.Clock()

player=py.Rect(0,0,50,50)
player.center=(400,500)
player_speed=5
enemy=py.Rect(0,0,60,60)
enemy.center=(400,200)

running=True
while running:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill((255,255,255))
    keys=py.key.get_pressed()
    if keys[py.K_a]:
        player.x -= player_speed
    if keys[py.K_d]:
        player.x += player_speed
    if keys[py.K_s]:
        player.y += player_speed
    if keys[py.K_w]:
        player.y -= player_speed

    player_ob = py.Rect(player.x, player.y, 50, 50)
    py.draw. rect(screen, (255,0,0), player_ob)
    
    enemy_ob = py.Rect(enemy.x, enemy.y, 50, 50)
    py.draw. rect(screen, (255,0,0), enemy_ob)
    py.display.flip()

py.quit()
sys.exit()