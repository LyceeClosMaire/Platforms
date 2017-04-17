# Créé par boivin, le 20/03/2017 en Python 3.2
import pygame
from pygame.locals import *

pygame.init()

horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((640, 480))
ouvert= True
sauter = 0

fond = pygame.image.load("background.jpg").convert()
fenetre.blit (fond, (0, 0))



perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

saut = -20
saut2 = -20

pygame.display.flip()
pygame.key.set_repeat(400, 30)
while ouvert :
    horloge.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            ouvert = False
        if event.type == KEYDOWN :
            if event.key == K_s :
                position_perso = position_perso.move(0,10)
            if event.key == K_d :
                position_perso = position_perso.move(10,0)
            if event.key == K_a :
                position_perso = position_perso.move(-10, 0)
            if sauter <=1 and event.key == K_SPACE :
                sauter = sauter+1
                if sauter == 2 and saut < 0:
                    saut = -saut




    if sauter==1 and saut2==-20:
        position_perso = position_perso.move(0, saut)
        saut = saut+1
        if saut > 20 :
            sauter = 0
            saut = -20
    if sauter ==2:
        position_perso = position_perso.move (0, saut2)
        saut2=saut2+1
        if saut2>20:
            sauter=sauter-1
            saut2 = -20


    fenetre.blit (fond, (0, 0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()

pygame.quit()