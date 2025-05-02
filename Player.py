from dis import Positions

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
        self.gravity_force = 1
        self.velocity_y = 0
        self.screen = screen


    def Move2DAndJump(self):
        keys = pygame.key.get_pressed()

        # Déplacement horizontal
        if keys[pygame.K_d]:
            self.Position.x += self.MaxSpeed

        if keys[pygame.K_q]:
            self.Position.x -= self.MaxSpeed
        pygame.draw.rect(self.screen, "red", (self.Position.x, self.Position.y, 10, 10))




