import game_world
import server
import pico2d

from ekey import *

class FireTempleEnter:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 560, -560

        if FireTempleEnter.image == None:
            FireTempleEnter.image = pico2d.load_image('Sprites/TempleEnter.png')

        self.CursorOn = False

    def draw(self):
        self.image.draw(self.x, self.y, 192, 224)

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy