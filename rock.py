import pico2d
import server
import random

class Rock:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 252, 252
        self.style = random.randint(1, 2)

        if Rock.image == None:
            Rock.image = pico2d.load_image('Sprites/Rock.png')

        self.hp = 15

    def draw(self):
        if self.style == 1:
            self.image.clip_draw(0, 0, 20, 20, self.x, self.y, 60, 60)
        elif self.style == 2:
            self.image.clip_draw(20, 0, 40, 20, self.x, self.y, 60, 60)

        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

    def get_bb(self):
        return self.x - 18, self.y - 20, self.x + 18, self.y + 10