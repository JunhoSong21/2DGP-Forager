import game_framework
import pico2d
import server

class Axe:
    image = None

    def __init__(self):
        self.x, self.y = 960, 557
        self.frame = 0
        self.imageDir = 1
        self.CursorOn = False

        self.axeRotate = 0.0
        self.axeRotate = max(self.axeRotate - game_framework.frame_time * 2, 0.0)

        if Axe.image == None:
            Axe.image = pico2d.load_image('Sprites/PickAxe.png')

        self.bgm1 = pico2d.load_wav('Sounds/Swing1.wav')
        self.bgm2 = pico2d.load_wav('Sounds/Swing2.wav')
        self.bgm3 = pico2d.load_wav('Sounds/Swing3.wav')
        self.bgm1.set_volume(32)
        self.bgm2.set_volume(32)
        self.bgm3.set_volume(32)

    def draw(self):
        if self.imageDir == -1:
            if self.frame == 0:
                self.image.draw(self.x + 12, self.y, 54, 54)
        elif self.imageDir == 1:
            if self.frame == 0:
                self.image.clip_composite_draw(0, 0, 18, 18, -self.axeRotate, 'h', self.x - 12, self.y, 54, 54)

    def update(self):
        self.imageDir = server.forager.imageDir

        if self.axeRotate <= 0.0:
            self.axeRotate = 0.0  # 고정
        else:
            self.axeRotate -= game_framework.frame_time * 5