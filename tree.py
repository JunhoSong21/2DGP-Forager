import pico2d
import server

class Tree:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = -252, 252

        if Tree.image == None:
            Tree.image = pico2d.load_image('Sprites/Tree.png')

        self.imageCursor = pico2d.load_image('Sprites/ObjectCursor.png')
        self.CursorOn = False
        self.hp = 10

    def draw(self):
        if (-112 < self.x - 960 < 112 and -112 < self.y - 540 < 112
            and -20 < server.mousecursor.x - self.x < 20 and -20 < server.mousecursor.y - self.y < 20):
            self.imageCursor.clip_draw(int(server.forager.frame) * 20, 0, 20, 20, self.x, self.y, 60, 60)
            self.CursorOn = True
        else:
            self.CursorOn = False

        self.image.draw(self.x, self.y + 32, 117, 132)
        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

    def get_bb(self):
        return self.x - 16, self.y - 24, self.x + 12, self.y + 2