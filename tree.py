import pico2d
import server

class Tree:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = -252, 280

        if Tree.image == None:
            Tree.image = pico2d.load_image('Sprites/Tree.png')

        self.hp = 10

    def draw(self):
        self.image.draw(self.x, self.y, 117, 132)
        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

    def get_bb(self):
        return self.x - 16, self.y - 56, self.x + 12, self.y - 30