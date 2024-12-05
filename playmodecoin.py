import game_framework
import pico2d

class PlayModeCoin:
    image = None

    def __init__(self):
        self.x, self.y = 50, 50
        if PlayModeCoin.image == None:
            PlayModeCoin.image = pico2d.load_image('Sprites/Coin.png')

    def draw(self):
        self.image.draw(self.x, self.y, 90, 90)

    def update(self):
        pass