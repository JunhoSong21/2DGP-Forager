import game_framework
import pico2d

class MainMenuExit:
    image = None

    def __init__(self):
        self.x, self.y = 560, 100
        if MainMenuExit.image == None:
            MainMenuExit.image = pico2d.load_image('Sprites/MainMenuExit.png')

    def draw(self):
        self.image.clip_draw(0, 0, 52, 25, self.x, self.y, 310, 150)

    def update(self):
        pass