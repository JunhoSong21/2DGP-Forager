import game_framework
import pico2d

class BackGround:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540
        if BackGround.image == None:
            BackGround.image = pico2d.load_image('Sprites/BackGroundLight.png')
    
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass