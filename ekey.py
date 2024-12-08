import game_world
import server
import pico2d

class Ekey:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 560, -560

        if Ekey.image == None:
            Ekey.image = pico2d.load_image('Sprites/Ekeyboard.png')

        self.CursorOn = False
        self.ImageOn = False

    def draw(self):
        if 930 < self.x < 990 and 550 < self.y < 650:
            self.ImageOn = True
            self.image.draw(self.x, self.y, 50, 50)
        else:
            self.ImageOn = False

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy