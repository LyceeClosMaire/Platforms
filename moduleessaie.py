# Créé par boivin, le 10/04/2017 en Python 3.2
import pygame
from pygame.locals import *

def module2pierre():

    pygame.init()

    horloge = pygame.time.Clock()
    fenetre = pygame.display.set_mode((1000, 750))
    ouvert= True
    sauter = 0

    fond = pygame.image.load("background.jpg").convert()
    fenetre.blit (fond, (0, 0))

    perso = pygame.image.load("perso.png").convert_alpha()
    position_perso = perso.get_rect()
    fenetre.blit(perso, position_perso)

    ligne = pygame.image.load("sol.png").convert_alpha()
    position_ligne = fenetre.blit (ligne, (0, 400))

    saut = -20

    while position_perso.left!=fond.left or position_perso.right!= fond.right :
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
                if sauter <1 and event.key == K_SPACE :
                    sauter = sauter+1

        if sauter == 1 :
            position_perso = position_perso.move(0, saut)
            saut = saut+1
            if position_perso.bottom > position_ligne.top : # pygame.sprite.collidesprite(perso, lignes)
                sauter = 0
                saut = -20
                position_perso.bottom = position_ligne.top



        fenetre.blit (fond, (0, 0))
        fenetre.blit(perso, position_perso)
        fenetre.blit (ligne, (0, 400))
        pygame.display.flip()

    pygame.quit()