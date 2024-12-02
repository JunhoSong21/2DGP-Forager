import game_framework
import pico2d

class BackGround:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540
    
    def draw(self):
        self.image.draw()

    def update(self):
        pass