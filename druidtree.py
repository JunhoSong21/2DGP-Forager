import server
import pico2d

class DruidTree:
    image = None

    def __init__(self):
        self.x, self.y = 540, 200

        if DruidTree.image == None:
            DruidTree.image = pico2d.load_image('Sprites/DruidTree.png')

    def draw(self):
        self.image.draw(1920 - server.forager.x + self.x, 1052 - server.forager.y + self.y, 516, 394)

    def update(self):
        pass