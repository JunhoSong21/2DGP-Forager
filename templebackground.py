import pico2d
import server

class TempleBackGround:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 0, 280
        self.CursorOn = False
        if TempleBackGround.image == None:
            TempleBackGround.image = pico2d.load_image('Sprites/templebackground.png')

        if TempleBackGround.bgm == None:
            TempleBackGround.bgm = pico2d.load_wav('Sounds/FireTemple.wav')

        TempleBackGround.bgm.set_volume(32)
        TempleBackGround.bgm.repeat_play()

    def draw(self):
        self.image.draw(1920 - server.forager.x + self.x, 1052 - server.forager.y + self.y, 560, 560)

    def update(self):
        pass