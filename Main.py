from Entitie import *
from Player import *
import pygame

from chunk import *



#intilaisation de la fenaitre pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
tailleDeLEcran = (screen.get_width(), screen.get_height())
print(tailleDeLEcran)
#création du joueur
Joueur = Player(100, 50, player_pos, 5, 10, "Bob",screen)
Prosedural = Chunck(screen)



#boucle principale du jeu

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")


    Prosedural.generation()
    Joueur.Move2DAndJump()

    




    pygame.display.flip()

    clock.tick(60)


pygame.quit()