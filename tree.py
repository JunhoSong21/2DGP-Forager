import game_framework
import game_world
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
        self.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 24)

        self.bgm1 = pico2d.load_wav('Sounds/HitTree1.wav')
        self.bgm2 = pico2d.load_wav('Sounds/HitTree2.wav')
        self.destroy = pico2d.load_wav('Sounds/TreeDestroy.wav')
        self.bgm1.set_volume(32)
        self.bgm2.set_volume(32)
        self.destroy.set_volume(32)

    def draw(self):
        if (-112 < self.x - 960 < 112 and -112 < self.y - 540 < 112
            and -20 < server.mousecursor.x - self.x < 20 and -20 < server.mousecursor.y - self.y < 20):
            self.imageCursor.clip_draw(int(server.forager.frame) * 20, 0, 20, 20, self.x, self.y, 60, 60)
            self.CursorOn = True
        else:
            self.CursorOn = False

        self.image.draw(self.x, self.y + 32, 117, 132)
        pico2d.draw_rectangle(*self.get_bb())

        self.font.draw(self.x - 15, self.y - 10, f'{self.hp}', (255, 255, 255))

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        if self.hp == 0:
            self.destroy.play(1)
            self.CursorOn = False
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 16, self.y - 24, self.x + 12, self.y + 2