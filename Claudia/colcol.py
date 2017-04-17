import pygame.locals
from pygame import *

pygame.init()
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((800,400), RESIZABLE)
winrect = fenetre.get_rect()
fond = pygame.image.load("Lava.jpg").convert()
perso = pygame.image.load("piq_91691_400x4004.png").convert_alpha()
gauche = winrect.left
droite = winrect.right
haut = winrect.top
bas = winrect.bottom

vit =10

x = 640
y = 200

persoRect = perso.get_rect(topleft=(x,y))
bloc = pygame.Rect(10,300,200,50)
col = [bloc]
sol = pygame.Rect(0,370,800,30)

continuer = True
while continuer == True:

    fenetre.blit(fond, (0,0))
    fenetre.fill((0,0,0) , sol)
    fenetre.fill( (140,27,27) , bloc)
    fenetre.blit(perso, persoRect)

    pygame.display.flip()

    persoSpeed = [0,0]

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_UP and not bloc.colliderect(persoRect) and not sol.colliderect(persoRect) :
                persoSpeed[1] -= vit
            if event.key == K_LEFT and (sol.colliderect(persoRect) and not bloc.colliderect(persoRect)) or (not sol.colliderect(persoRect) and bloc.colliderect(persoRect)):
                persoSpeed[0] -= vit
            if event.key == K_DOWN and not bloc.colliderect(persoRect) and not sol.colliderect(persoRect):
                persoSpeed[1] += vit
            if event.key == K_RIGHT and not bloc.colliderect(persoRect) and sol.colliderect(persoRect) or not sol.colliderect(persoRect) and bloc.colliderect(persoRect):
                persoSpeed[0] += vit

    persoRect.move_ip(persoSpeed)
    if bloc.colliderect(persoRect):
         if persoRect.left < bloc.left < persoRect.right or persoRect.left < bloc.right < persoRect.right :
            persoRect.left = bloc.right
         else:
            persoRect.midbottom = bloc.midtop


    clock.tick(60)
pygame.quit()