from chunk import *
from Entitie import *
import pygame



class Player(Entitie):
    def __init__(self, health, stamina, Position, max_speed, damage, name,screen):
        super().__init__(health, stamina, max_speed, damage, name)
        self.health = health
        self.stamina = stamina
        self.Position = Position
        self.level = 1
        self.is_jumping = False
        self.jump_force = -7
        self.gravity_force = 9.8
        self.velocity_y = 0
        self.screen = screen
        self.VectorGravity = (0,1)


    def Move2DAndJump(self):
        keys = pygame.key.get_pressed()

        # Déplacement horizontal




        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = self.jump_force

        pygame.draw.rect(self.screen, "red", (self.Position[0],self.Position[1], 10, 10))



    def gravity(self):
        gravity = [self.Position[0], self.VectorGravity[1] * self.velocity_y + self.Position[1]]

        self.Position[1] = gravity[1]
        if not self.Position[1] >= 660:
            self.velocity_y += self.gravity_force*0.051


        else:
            self.velocity_y = 0
            self.is_jumping = False

    def Colision(self):


        couleur_du_pixel = self.screen.get_at((int(self.Position[0]), int(self.Position[1] + 10)))

        if couleur_du_pixel == (139, 69, 19):
            self.velocity_y = 0
            self.is_jumping = False
        elif couleur_du_pixel == (34, 139, 34):
            self.velocity_y = 0
            self.is_jumping = False
        elif couleur_du_pixel == (34, 139, 34):
            self.velocity_y = 0
            self.is_jumping = False
        elif couleur_du_pixel ==(105, 105, 105):
            self.velocity_y = 0
            self.is_jumping = False

