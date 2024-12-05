import game_framework
import pico2d

class MainMenuPlay:
    image = None

    def __init__(self):
        self.x, self.y = 384, 930
        if MainMenuPlay.image == None:
            MainMenuPlay.image = pico2d.load_image('Sprites/MainMenuPlay.png')

        self.bgm = pico2d.load_wav('Sounds/Forest2.wav')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0, 0, 104, 33, self.x, self.y, 624, 198)

    def update(self):
        pass