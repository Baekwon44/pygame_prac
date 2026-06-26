import pygame as py
import sys

py.init()
screen=py.display.set_mode((800,400))
clock=py.time.Clock()

rect_x, rect_y = 200,100
target_rect = py.Rect(500,200,40,40)
score = 0
game_font = py.font.SysFont(None,40)

running=True
while running:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False
    screen.fill((255,255,255))



    keys=py.key.get_pressed()
    if keys[py.K_a]:
        rect_x -= 5
    if keys[py.K_d]:
        rect_x += 5
    if keys[py.K_w]:
        rect_y -= 5
    if keys[py.K_s]:
        rect_y += 5

    player_rect = py.Rect(rect_x, rect_y, 50, 50)
    
    py.draw.rect(screen, (255,0,0), player_rect)
    py.draw.rect(screen, (0,0,255), target_rect)
    score_surface = game_font.render(f"Score : {score}", True, (0,0,0))
    screen.blit(score_surface,(10,10))

    if player_rect.colliderect(target_rect):
        score += 10
        target_rect.x, target_rect.y = 999,999

    py.display.flip()

py.quit()
sys.exit()