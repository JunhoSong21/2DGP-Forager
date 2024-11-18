import game_framework
import pico2d

class MainMenuExtras:
    image = None

    def __init__(self):
        self.x, self.y = 394, 750
        if MainMenuExtras.image == None:
            MainMenuExtras.image = pico2d.load_image('Sprites/MainMenuExtras.png')

    def draw(self):
        self.image.clip_draw(0, 0, 99, 26, self.x, self.y, 594, 144)

    def update(self):
        pass