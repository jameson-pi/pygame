#setup
import pygame
from pygame.locals import *
pygame.init()
#vars
s_width =1000
s_height = 1000
screen= pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Platfomer")

sun = pygame.image.load("img/sun.png")
sky = pygame.image.load("img/sky.jpg")
player = pygame.Rect((300,250,50,50))
#loop
run=True
while run:
    screen.fill((0,0,0))
    screen.blit(sky,(0,0))
    screen.blit(sun,(100,100))
    pygame.draw.rect(screen, (255,0,0),player)
    key=pygame.key.get_pressed()
    if key[pygame.K_a]== True:
        player.move_ip(-1,0)
    elif key[pygame.K_w]== True:
        player.move_ip(0,-1)
    elif key[pygame.K_s]== True:
        player.move_ip(0,1)
    elif key[pygame.K_d]== True:
        player.move_ip(1,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()