import game_framework
import game_world
import pico2d

class Gameover:
    image = None

    def __init__(self):
        self.x, self.y = 960, 540

        if Gameover.image == None:
            Gameover.image = pico2d.load_image('Sprites/DamageScreen.png')

        self.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 50)

    def draw(self):
        self.image.draw(self.x, self.y, 1920, 1080)

        self.font.draw(self.x - 200, self.y, f'Game Over!', (255, 255, 255))

    def update(self):
        pass