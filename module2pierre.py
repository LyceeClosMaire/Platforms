# Créé par boivin, le 03/04/2017 en Python 3.2
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

    perso_image = pygame.image.load("perso.png").convert_alpha()

    class Perso(pygame.sprite.Sprite):
        def __init__ (self, position):
            super().__init__()

            self.image = perso_image
            self.rect = self.image.get_rect(topleft = position)


    ligne = pygame.image.load("sol.png").convert_alpha()
    position_ligne = fenetre.blit (ligne, (0, 400))

    class Ligne(pygame.sprite.Sprite):
        def __init__(self, position):
            super().__init__()

            self.image = ligne
            self.rect = self.image.get_rect(topleft = position)

    lignes = pygame.sprite.Group( Ligne( (0,400) ) )
    perso = Perso( (0,0) )

    saut = -20
    yperso = 0

    pygame.display.flip()
    pygame.key.set_repeat(400, 30)
    while ouvert :
        horloge.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                ouvert = False
            if event.type == KEYDOWN :
                if event.key == K_s :
                    perso.rect = perso.rect.move(0,10)
                if event.key == K_d :
                    perso.rect = perso.rect.move(10,0)
                if event.key == K_a :
                    perso.rect = perso.rect.move(-10, 0)
                if sauter <1 and event.key == K_SPACE :
                    sauter = sauter+1

        if sauter == 1 :
            perso.rect = perso.rect.move(0, saut)
            saut = saut+1
            if pygame.sprite.spritecollide(perso, lignes, False):
                sauter = 0
                saut = -20
                perso.rect.bottom = position_ligne.top

        if perso.rect.bottom != position_ligne.top and sauter == 0 :
            yperso = yperso +1
            perso.rect = perso.rect.move(0, yperso)

        fenetre.blit (fond, (0, 0))
        fenetre.blit(perso.image, perso.rect)
        lignes.draw(fenetre)
        pygame.display.flip()

    pygame.quit()