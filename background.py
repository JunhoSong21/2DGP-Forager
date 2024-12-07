import game_framework
import pico2d

class BackGround:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540
        self.CursorOn = False
        
        if BackGround.image == None:
            BackGround.image = pico2d.load_image('Sprites/BackGroundLight.png')

        self.bgm = pico2d.load_wav('Sounds/Forest1.wav')
        self.bgm.set_volume(32)
        #self.bgm.repeat_play()
    
    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass