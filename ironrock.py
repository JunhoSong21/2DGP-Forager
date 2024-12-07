import game_world
import pico2d
import server
import random

from ironrockdrop import *

class IronRock:
    image = None
    destroy = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 56, 0
        self.style = random.randint(1, 2)

        if IronRock.image == None:
            IronRock.image = pico2d.load_image('Sprites/IronRock.png')

        self.imageCursor = pico2d.load_image('Sprites/ObjectCursor.png')
        self.CursorOn = False
        self.hp = 9
        self.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 24)

        self.bgm1 = pico2d.load_wav('Sounds/HitRock1.wav')
        self.bgm2 = pico2d.load_wav('Sounds/HitRock2.wav')
        self.bgm1.set_volume(32)
        self.bgm2.set_volume(32)

        if IronRock.destroy == None:
            IronRock.destroy = pico2d.load_wav('Sounds/RockDestroy.wav')
            IronRock.destroy.set_volume(60)

    def draw(self):
        if (-112 < self.x - 960 < 112 and -112 < self.y - 540 < 112
            and -20 < server.mousecursor.x - self.x < 20 and -20 < server.mousecursor.y - self.y < 20):
            self.imageCursor.clip_draw(int(server.forager.frame) * 20, 0, 20, 20, self.x, self.y, 60, 60)
            self.CursorOn = True
        else:
            self.CursorOn = False
    
        if self.style == 1:
            self.image.clip_draw(0, 0, 20, 20, self.x, self.y, 60, 60)
        elif self.style == 2:
            self.image.clip_draw(20, 0, 40, 20, self.x, self.y, 60, 60)

        pico2d.draw_rectangle(*self.get_bb())

        self.font.draw(self.x - 5, self.y - 10, f'{self.hp}', (255, 255, 255))

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        if self.hp == 0:
            IronRock.destroy.play()
            self.CursorOn = False
            ironrockdrop = IronRockDrop()
            game_world.add_object(ironrockdrop, 2)
            ironrockdrop.cx, ironrockdrop.cy = self.cx, self.cy
            game_world.add_collision_pair('forager:ironrockdrop', None, ironrockdrop)
            game_world.add_collision_pair('forager:ironrockdrop', server.forager, None)
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 18, self.y - 20, self.x + 18, self.y + 10