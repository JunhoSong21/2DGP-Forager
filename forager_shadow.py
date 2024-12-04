import game_framework
import game_world
import pico2d

class ForagerShadow:
    image = None

    def __init__(self):
        self.x, self.y = 384, 930
        
        if ForagerShadow.image == None:
            ForagerShadow.image = pico2d.load_image('Sprites/ForagerShadow.png')

    def draw(self):
        self.image.draw(self.x, self.y, 96, 96)

    def update(self):
        pass