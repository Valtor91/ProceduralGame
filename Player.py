
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
        self.jump_force = -20
        self.gravity_force = 9.8

        self.screen = screen
        self.VectorGravity = (0,1)

    def Move2DAndJump(self):
        keys = pygame.key.get_pressed()

        # Déplacement horizontal
        if keys[pygame.K_d]:
            self.Position[0] += self.MaxSpeed

        if keys[pygame.K_q]:
            self.Position[0] -= self.MaxSpeed
        pygame.draw.rect(self.screen, "red", (self.Position[0],self.Position[1], 10, 10))
        print(self.Position)
    def gravity(self):
        if not self.Position[1] >= 660:
            gravity = [self.Position[0], self.VectorGravity[1]*self.gravity_force + self.Position[1]]

            self.Position[1] = gravity[1]
        else:
            self.Position[1] = 660



