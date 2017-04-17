# Créé par CHAVANSOT, le 03/04/2017 en Python 3.2
import pygame
import pygame.mixer
import font
from pygame.locals import *
def f_settings():
    pygame.init()
    pygame.display.set_caption("PlatISN")
    fenetre = pygame.display.set_mode( (1000,750) )
    ouvert = True

    fond = pygame.image.load("background.jpg").convert()
    retour = pygame.image.load("retour.png").convert_alpha()
    position_retour = retour.get_rect(center = (500,150) )
    s_son = pygame.image.load("son.png").convert_alpha()
    position_son = s_son.get_rect(center =(250,375))
    while ouvert:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if position_retour.collidepoint(x, y):
                    font.font()
               # if position_son.collidepoint(x, y):

            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                ouvert = False


        fenetre.blit(fond, (0,0))
        fenetre.blit(retour,position_retour)
        fenetre.blit(s_son,position_son)
        pygame.display.flip()
    pygame.quit()