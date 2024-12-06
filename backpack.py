import pico2d
import server

class BackPack:
    image = None

    def __init__(self):
        self.x, self.y = 960, 565
        self.frame = 0
        self.imageDir = 1
        self.moving = False

        if BackPack.image == None:
            BackPack.image = pico2d.load_image('Sprites/BackPack.png')

    def draw(self):
        frameX = int(self.frame) * 15

        if self.moving == False:
            if self.imageDir == 1:
                self.image.clip_draw(frameX, 20, 15, 40, self.x, self.y, 45, 60)
            elif self.imageDir == -1:
                self.image.clip_composite_draw(frameX, 20, 15, 40, 0, 'h', self.x, self.y, 45, 60)
        elif self.moving == True:
            if self.imageDir == 1:
                self.image.clip_draw(frameX, 0, 15, 20, self.x, self.y, 45, 60)
            elif self.imageDir == -1:
                self.image.clip_composite_draw(frameX, 0, 15, 20, 0, 'h', self.x, self.y, 45, 60)

    def update(self):
        self.frame = server.forager.frame
        self.imageDir = server.forager.imageDir