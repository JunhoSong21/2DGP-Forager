import pico2d
import server
from forager import *

class GrassLand:
    def __init__(self):
        self.image = pico2d.load_image('Sprites/GrassLandSquare.png')    

    def draw(self):
        self.image.draw(1920 - server.forager.x, 1080 - server.forager.y, 560, 588)

    def update(self):
        pass
    