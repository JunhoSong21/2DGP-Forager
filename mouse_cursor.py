import game_framework
import game_world
import pico2d

class MouseCursor:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540
        self.size = 0
        self.CursorOn = False

        if MouseCursor.image == None:
            MouseCursor.image = pico2d.load_image('Sprites/MouseCursor.png')

    def draw(self):
        if self.size == 0:
            self.image.draw(self.x + 16, self.y - 16, 48, 48)
        elif self.size == 1:
            self.image.draw(self.x + 20, self.y - 20, 40, 40)

    def update(self):
        pass