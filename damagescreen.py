import game_framework
import game_world
import pico2d

class DamageScreen:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 960, 540

        self.starttime = pico2d.get_time()

        if DamageScreen.image == None:
            DamageScreen.image = pico2d.load_image('Sprites/DamageScreen.png')

        if DamageScreen.bgm == None:
            DamageScreen.bgm = pico2d.load_wav('Sounds/PlayerDamage.wav')
            DamageScreen.bgm.set_volume(60)

    def draw(self):
        self.image.draw(self.x, self.y, 1920, 1080)

    def update(self):
        if pico2d.get_time() - self.starttime >= 0.1:
            DamageScreen.bgm.play()
            game_world.remove_object(self)