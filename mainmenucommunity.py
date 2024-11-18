import game_framework
import pico2d

class MainMenuCommunity:
    image = None

    def __init__(self):
        self.x, self.y = 384, 445
        if MainMenuCommunity.image == None:
            MainMenuCommunity.image = pico2d.load_image('Sprites/MainMenuCommunity.png')

    def draw(self):
        self.image.clip_draw(0, 0, 98, 23, self.x, self.y, 572, 138)

    def update(self):
        pass