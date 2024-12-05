import game_framework
import pico2d

class MainMenuSelect:
    def __init__(self):
        self.bgm = pico2d.load_wav('Sounds/MainMenuSelect.wav')
        self.bgm.set_volume(32)
        self.bgm.play(1)
    
    def draw(self):
        pass

    def update(self):
        pass