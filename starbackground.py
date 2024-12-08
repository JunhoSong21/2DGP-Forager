import game_world
import pico2d

class StarBackGround:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540
        self.CursorOn = False
        if StarBackGround.image == None:
            StarBackGround.image = pico2d.load_image('Sprites/StarBackGround.png')

    def draw(self):
        self.image.draw(self.x, self.y, 1920, 1080)

    def update(self):
        pass