import game_framework
import server
import pico2d
import random
import math

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Slime:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, 0
        self.frame = random.randint(0, 4)
        self.CursorOn = False

        if Slime.image == None:
            Slime.image = pico2d.load_image('Sprites/Slime.png')

        self.imageCursor = pico2d.load_image('Sprites/ObjectCursor.png')
        self.hp = 5
        self.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 24)

    def draw(self):
        if (-112 < self.x - 960 < 112 and -112 < self.y - 540 < 112
            and -20 < server.mousecursor.x - self.x < 20 and -20 < server.mousecursor.y - self.y < 20):
            self.imageCursor.clip_draw(int(server.forager.frame) * 20, 0, 20, 20, self.x, self.y, 60, 60)
            self.CursorOn = True
        else:
            self.CursorOn = False

        frameX = int(self.frame) * 16
        self.image.clip_draw(frameX, 0, 16, 16, self.x, self.y, 32, 32)

        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if 860 < self.x < 1060 and 440 < self.y < 640:
            if self.x < 960:
                self.cx += 0.1
            elif self.x > 960:
                self.cx -= 0.1
            if self.y < 540:
                self.cy += 0.1
            elif self.y > 540:
                self.cy -= 0.1

    def get_bb(self):
        return self.x - 12, self.y - 15, self.x + 12, self.y
    
    def handle_collision(self, group, other):
        if group == 'forager:slime':
            pass