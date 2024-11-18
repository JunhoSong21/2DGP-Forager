import game_framework
import pico2d

class MainMenuLogo:
    image = None

    def __init__(self):
        self.x, self.y = 960, 960
        if MainMenuLogo.image == None:
            MainMenuLogo.image = pico2d.load_image('Sprites/ForagerLogo.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1920, 1037, self.x, self.y, 640, 345)

    def update(self):
        pass