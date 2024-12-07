import game_framework
import game_world
import pico2d
from state_machine import *
import math
import random

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Idle:
    @staticmethod
    def enter(forager, e):
        forager.moving = False
        forager.speed = 0
        forager.frame = 0
        forager.dir = 0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunRight:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = 0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunRightUp:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = math.pi / 4.0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunRightDown:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = -math.pi / 4.0
        
    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunLeft:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = math.pi
        
    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunLeftUp:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = math.pi * 3.0 / 4.0
        
    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunLeftDown:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = -math.pi * 3.0 / 4.0
        
    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunUp:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = math.pi / 2.0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class RunDown:
    @staticmethod
    def enter(forager, e):
        forager.moving = True
        forager.speed = RUN_SPEED_PPS
        forager.dir = -math.pi / 2.0

    @staticmethod
    def exit(forager, e):
        pass

    @staticmethod
    def do(forager):
        pass

class Forager:
    def __init__(self):
        self.x, self.y = 960, 540
        self.frame = 0
        self.image = pico2d.load_image('Sprites/PlayerSprite.png')
        self.imageDir = 1
        self.moving = False
        self.speed = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {d_down: RunRight, a_down: RunLeft, a_up: RunRight, d_up: RunLeft, w_down: RunUp, s_down: RunDown, w_up: RunDown, s_up: RunUp},
                RunRight: {d_up: Idle, a_down: Idle, w_down: RunRightUp, w_up: RunRightDown, s_down: RunRightDown, s_up: RunRightUp},
                RunRightUp: {w_up: RunRight, d_up: RunUp, a_down: RunUp, s_down: RunRight},
                RunUp: {w_up: Idle, a_down: RunLeftUp, s_down: Idle, d_down: RunRightUp, a_up: RunRightUp, d_up: RunLeftUp},
                RunLeftUp: {d_down: RunUp, s_down: RunLeft, a_up: RunUp, w_up: RunLeft},
                RunLeft: {a_up: Idle, w_down: RunLeftUp, d_down: Idle, s_down: RunLeftDown, w_up: RunLeftDown, s_up: RunLeftUp},
                RunLeftDown: {a_up: RunDown, s_up: RunLeft, w_down: RunLeft, d_down: RunDown},
                RunDown: {s_up: Idle, a_down: RunLeftDown, w_down: Idle, d_down: RunRightDown, a_up: RunRightDown, d_up: RunLeftDown},
                RunRightDown: {d_up: RunDown, s_up: RunRight, a_down: RunDown, w_down: RunRight}
            }
        )

        self.bgm1 = pico2d.load_wav('Sounds/Walk1.wav')
        self.bgm2 = pico2d.load_wav('Sounds/Walk2.wav')
        self.bgm1.set_volume(32)
        self.bgm2.set_volume(32)
        

        self.image_heart = pico2d.load_image('Sprites/Heart.png')
        self.heart_x, self.heart_y = 40, 1040
        self.heart = 3

        self.image_coin = pico2d.load_image('Sprites/Coin.png')
        self.coin_x, self.coin_y = 40, 40
        self.coin = 0

        self.itemCount = 1

    def update(self):
        self.state_machine.update()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += math.cos(self.dir) * self.speed * game_framework.frame_time
        self.y += math.sin(self.dir) * self.speed * game_framework.frame_time
        
        if self.moving == True and int(self.frame) == 3 :
            x = random.randint(1, 2)

            if x == 1:
                self.bgm1.play(1)
            elif x == 2:
                self.bgm2.play(1)

    def add_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        frameX = int(self.frame) * 15

        cx, cy = 960, 562

        if self.moving == False:
            if self.imageDir == 1:
                self.image.clip_draw(frameX, 20, 15, 40, cx, cy, 45, 60)
            elif self.imageDir == -1:
                self.image.clip_composite_draw(frameX, 20, 15, 40, 0, 'h', cx, cy, 45, 60)
        elif self.moving == True:
            if self.imageDir == 1:
                self.image.clip_draw(frameX, 0, 15, 20, cx, cy, 45, 60)
            elif self.imageDir == -1:
                self.image.clip_composite_draw(frameX, 0, 15, 20, 0, 'h', cx, cy, 45, 60)

        if self.heart >= 1:
            self.image_heart.clip_draw(0, 0, 36, 36, self.heart_x, self.heart_y, 60, 60)
        if self.heart >= 2:
            self.image_heart.clip_draw(0, 0, 36, 36, self.heart_x + 65, self.heart_y, 60, 60)
        if self.heart >= 3:
            self.image_heart.clip_draw(0, 0, 36, 36, self.heart_x + 130, self.heart_y, 60, 60)

        pico2d.draw_rectangle(*self.get_bb())

        self.image_coin.draw(self.coin_x, self.coin_y, 90, 90)

    def set_item(self, item):
        self.item = item

    def get_bb(self):
        return 947, 532, 973, 552
