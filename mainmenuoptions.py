import game_framework
import pico2d

class MainMenuOptions:
    image = None

    def __init__(self):
        self.x, self.y = 220, 100
        if MainMenuOptions.image == None:
            MainMenuOptions.image = pico2d.load_image('Sprites/MainMenuOptions.png')
            
    def draw(self):
        self.image.clip_draw(0, 0, 72, 25, self.x, self.y, 428, 150)

    def update(self):
        pass