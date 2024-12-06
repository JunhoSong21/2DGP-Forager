import pico2d
from forager import *

class GrassLand:
    def __init__(self):
        self.image = pico2d.load_image('Sprites/GrassLand.png')
        self.x, self.y = Forager.x, Forager.y
        

    def draw(self):
        self.image.draw(960, 540, 560, 588)

    def update(self):
        pass
    