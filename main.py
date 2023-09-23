from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40  # frame rate
ani = 4  # animation cycles
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0
        self.images = []

        img = pygame.image.load(os.path.join('img', 'penguin_walk04.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def move(self, x, y):
        self.movex += x
        self.movey += y
    def gravity(self):
        self.movey += 3.2 # how fast player falls
        
        if self.rect.y > worldy and self.movey >= 0:
            self.movey = 0
            self.rect.y = worldy-ty-ty
'''
Setup
'''

backdrop = pygame.image.load(os.path.join('img', 'sky.jpg'))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    key=pygame.key.get_pressed()
    if key[pygame.K_a]== True:
        player.move(-1,0)
    elif key[pygame.K_w]== True:
        player.move(0,-1)
    elif key[pygame.K_s]== True:
        player.move(0,1)
    elif key[pygame.K_d]== True:
        player.move(1,0)
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)