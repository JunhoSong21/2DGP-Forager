import game_framework
import game_world
import pico2d

class MouseCursor:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540

        if MouseCursor.image == None:
            MouseCursor.image = pico2d.load_image('Sprites/MouseCursor.png')

    def draw(self):
        self.image.draw(self.x + 16, self.y - 16, 48, 48)

    def update(self):
        pass