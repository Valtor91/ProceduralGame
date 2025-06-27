import pygame
from PIL import Image, ImageDraw
import noise
import random

class Chunck:
    def __init__(self, screen):
        global Value1D,Value2D
        self.screen = screen
        self.Black = (0, 0, 0)  # Grottes
        self.Dirt = (139, 69, 19)  # Terre
        self.Rock = (105, 105, 105)  # Roche
        self.Grass = (34, 139, 34)  # Herbe

        self.Scale = 300
        self.Octave = 3
        self.Lacunarity = 2.0
        self.Persistence = 0.7
        self.seed = random.randint(0, 400)
        self.perlin = False
        self.gene = []
        self.ground_level = screen.get_height() /2
        self.avencer = 0
        self.color = (255,255,255)
        self.Value2D = 0
        self.get_width = self.screen.get_width()

    def PerlinNoise(self):


        noise_surface = pygame.Surface((self.get_width, self.screen.get_height()))




        for x in range(0,self.get_width,10):
            Value1D = int(self.ground_level + noise.pnoise1(x / self.Scale, octaves=self.Octave, base=self.seed) * 100)

            for y in range(0,self.screen.get_height(),10):
                if y < Value1D:
                    self.color = (135, 206, 250)
                elif y == Value1D:
                    self.color = self.Grass
                elif y >= Value1D + 20:
                    self.color = self.Rock


                    if y >= Value1D+40:

                        self.Value2D = noise.pnoise2(
                            x / self.Scale,
                            y / self.Scale,
                            octaves=self.Octave,
                            persistence=self.Persistence,
                            lacunarity=self.Lacunarity,
                            repeatx=self.screen.get_width(),
                            repeaty=self.screen.get_height(),
                            base=self.seed
                        )
                        if self.Value2D >= 0.2:
                            self.color = (109, 109, 109  )
                        else:
                            self.color = (71, 71, 71  )

                elif y > Value1D:
                    self.color = self.Dirt



                pygame.draw.rect(noise_surface, self.color, pygame.Rect(x, y, 10, 10))

        return noise_surface






    def generation(self):


        if not self.perlin:


            self.gene= self.PerlinNoise()
            print(self.gene)
            self.perlin = True


        keys = pygame.key.get_pressed()
        self.screen.blit(self.gene, (self.avencer, 0))
        if keys[pygame.K_q]:
            self.avencer += 5
            self.screen.blit(self.gene, (self.avencer, 0))
            self.get_width = self.get_width + 10

            print(self.get_width)



        if keys[pygame.K_d]:
            self.avencer -= 5
            self.screen.blit(self.gene, (self.avencer, 0))
            self.get_width = self.get_width + 10
            print(self.get_width)
            width = self.screen.get_width()


            x_pixel = width - 1


            couleur_du_pixel = self.screen.get_at((x_pixel, 0))
            print(couleur_du_pixel)
            if couleur_du_pixel == (135, 206, 250):
                self.perlin = True
            else:
                self.perlin = False