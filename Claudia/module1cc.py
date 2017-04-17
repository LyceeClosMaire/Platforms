import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((284, 177))
fond = pygame.image.load("images.jpg").convert()
fenetre.blit(fond, (0,0))

pygame.display.flip()

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            continuer = False

