from PIL import Image, ImageDraw
import noise

Shape = (1280, 720)
Scale = 25.0
Octave = 2
Lacunari = 2.0
Persistence = 1.2

""""for x in range (Shape[0]):
    for y in range (Shape[1]):
        Value = noise.pnoise2( x/Scale,
                            y/Scale,
                            octaves = Octave,
                            persistence = Persistence,
                            lacunarity = Lacunari,
                            repeatx = Shape[0],
                            repeaty = Shape[1],
                            base = 0)
        print(Value)"""

