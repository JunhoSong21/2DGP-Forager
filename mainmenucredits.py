import game_framework
import pico2d

class MainMenuCredits:
    image = None

    def __init__(self):
        self.x, self.y = 384, 280
        if MainMenuCredits.image == None:
            MainMenuCredits.image = pico2d.load_image('Sprites/MainMenuCredits.png')

    def draw(self):
        self.image.clip_draw(0, 0, 83, 22, self.x, self.y, 498, 132)

    def update(self):
        pass