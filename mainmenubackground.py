import game_framework
import pico2d

class MainMenuBackground:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540
        self.speed = 50
        if MainMenuBackground.image == None:
            MainMenuBackground.image = pico2d.load_image('Sprites/MainMenuBackground.png')

    def draw(self):
        self.image.clip_draw(0, 0, 312, 180, self.x, self.y, 1920, 1080)

    def update(self):
        self.x += self.speed * 1 * game_framework.frame_time

        if self.x >= 2880:
            self.x = -960