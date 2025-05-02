import pygame
class Entitie:
    def __init__(self, heath, stamina, MaxSpeed, Damage, name):
        self.Name = name
        self.Health = heath
        self.Stamina = stamina
        self.MaxSpeed = MaxSpeed
        self.Damage = Damage
    def Move2D(self, MaxSpeed):
        pass

    def Damage(self,Damage, Health):
        Health -= Damage
        return Health

    def Death(self,Health):
        if Health <= 0:
            return True
        else:
            return False



