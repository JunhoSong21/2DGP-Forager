import pico2d
import server

class Axe:
    image = None

    def __init__(self):
        self.x, self.y = 960, 557
        self.frame = 0
        self.imageDir = 1

        if Axe.image == None:
            Axe.image = pico2d.load_image('Sprites/PickAxe.png')

    def draw(self):
        if self.imageDir == -1:
            if self.frame == 0:
                self.image.draw(self.x + 12, self.y, 54, 54)
        elif self.imageDir == 1:
            if self.frame == 0:
                self.image.clip_composite_draw(0, 0, 18, 18, 0, 'h', self.x - 12, self.y, 54, 54)

    def update(self):
        self.imageDir = server.forager.imageDir