    # Créé par CHAVANSOT, le 13/03/2017 en Python 3.2
import pygame
import pygame.mixer
from pygame.locals import *
import module2pierre
import settings

def font():
    pygame.init()

    pygame.display.set_caption("PlatISN")
    fenetre = pygame.display.set_mode( (1000,750) )
    ouvert = True

    fond = pygame.image.load("background.jpg").convert()

    start = pygame.image.load("start.png").convert_alpha()
    position_start = start.get_rect(center = (500,375) )

    s_settings = pygame.image.load("settings.png").convert_alpha()
    position_settings = s_settings.get_rect()
    position_settings.center = 50,700

    logo = pygame.image.load("logo.png").convert_alpha()
    position_logo = logo.get_rect()
    position_logo.center = 500,150

    while ouvert:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if position_start.collidepoint(x, y):
                    module2pierre.module2pierre()
                if position_settings.collidepoint(x, y):
                    settings.f_settings()
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
             ouvert = False

        fenetre.blit(fond, (0,0))
        fenetre.blit(start,position_start)
        fenetre.blit(s_settings,position_settings)
        fenetre.blit(logo,position_logo)

        pygame.display.flip()

    pygame.quit()

