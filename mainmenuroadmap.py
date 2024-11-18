import game_framework
import pico2d

class MainMenuRoadmap:
    image = None

    def __init__(self):
        self.x, self.y = 384, 595
        if MainMenuRoadmap.image == None:
            MainMenuRoadmap.image = pico2d.load_image('Sprites/MainMenuRoadmap.png')
    
    def draw(self):
        self.image.clip_draw(0, 0, 95, 26, self.x, self.y, 560, 144)

    def update(self):
        pass