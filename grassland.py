import pico2d
import server
from forager import *

class GrassLand:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = pico2d.load_image('Sprites/GrassLandSquare.png')   
        self.CursorOn = False

    def draw(self):
        self.image.draw(1920 - server.forager.x + self.x, 1052 - server.forager.y + self.y, 560, 588)

    def update(self):
        pass
    