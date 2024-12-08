import game_framework
import game_world
import pico2d
from state_machine import *
import math
import random

from grassland import *
from tree import *
from druidtree import *
from slime import *
from demon import *
from firetempleenter import *
from damagescreen import *

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6
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
        self.CursorOn = False
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

        #걷는소리 2종 랜덤
        self.bgm1 = pico2d.load_wav('Sounds/Walk1.wav')
        self.bgm2 = pico2d.load_wav('Sounds/Walk2.wav')
        self.bgm1.set_volume(32)
        self.bgm2.set_volume(32)
        
        #화면 좌상단 하트
        self.image_heart = pico2d.load_image('Sprites/Heart.png')
        self.heart_x, self.heart_y = 40, 1040
        self.heart = 3

        #화면 좌하단 코인
        self.image_coin = pico2d.load_image('Sprites/Coin.png')
        self.coin_x, self.coin_y = 40, 40
        self.coin = 0

        #코인 숫자
        self.font_coin = pico2d.load_font('Sprites/DungGeunMo.ttf', 60)
        self.font_coin.x, self.font_coin.y = 90, 45

        #화면 하단 인벤토리
        self.image_useItemSlot = pico2d.load_image('Sprites/PlaymodeInventory.png')
        self.useItemSlot_x, self.useItemSlot_y = 960, 50
        self.image_useItem = pico2d.load_image('Sprites/Pickaxe.png')
        #self.image_useItem2 = pico2d.load_image('Sprites/Sword1.png')
        
        self.useItemSlot = 1 # 사용중인 아이템 슬롯
        self.useItemCount = 1 # 인벤토리 아이템 개수

        # 나무 자원
        self.woodCount = 0

        # 돌 자원
        self.rockCount = 0

        # 철 자원
        self.ironrockCount = 0

        # 금 자원
        self.goldrockCount = 0

        # 진행 페이즈
        self.phase = 1

        # 피격 간격 조절
        self.damage_can = True
        self.damage_time = 0.0
        self.heart_time = 0.0

    def update(self):
        self.state_machine.update()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += math.cos(self.dir) * self.speed * game_framework.frame_time
        self.y += math.sin(self.dir) * self.speed * game_framework.frame_time
        
        if self.moving == True and int(self.frame) == 2:
            x = random.randint(1, 2)

            if x == 1:
                self.bgm1.play(1)
            elif x == 2:
                self.bgm2.play(1)

        if self.heart < 3 and pico2d.get_time() - self.heart_time >= 10.0:
            self.heart += 1

        if self.damage_can == False and pico2d.get_time() - self.damage_time >= 2.0:
            self.damage_can = True

        if self.coin >= 3 and self.phase == 1: # 두번째 페이즈
            self.coin -= 3

            grassland2 = GrassLand()
            game_world.add_object(grassland2, 1)
            grassland2.x, grassland2.y = 560, 0
            druidtree = DruidTree()
            game_world.add_object(druidtree, 2)
            tree = Tree()
            game_world.add_object(tree, 2)
            tree.cx, tree.cy = 560, -254

            self.phase = 2

        elif self.coin >= 5 and self.phase == 2:
            self.coin -= 5
            self.phase = 3

            grassland3 = GrassLand()
            game_world.add_object(grassland3, 1)
            grassland3.x, grassland3.y = 0, -560

            grassland4 = GrassLand()
            game_world.add_object(grassland4, 1)
            grassland4.x, grassland4.y = 560, -560

            slimes = [Slime() for _ in range(5)]
            for slime in slimes:
                slime.cx = random.randint(-280, 280)
                slime.cy = random.randint(-840, -280)
                game_world.add_object(slime, 2)
                game_world.add_collision_pair('forager:slime', None, slime)
                game_world.add_collision_pair('forager:slime', server.forager, None)

            firetemple = FireTempleEnter()
            game_world.add_object(firetemple, 2)
            #self.useItemCount = 2

        elif self.phase == 4:
            self.phase = 5
            demons = [Demon() for _ in range(6)]
            for demon in demons:
                demon.cx = random.randint(-240, 240)
                demon.cy = random.randint(100, 450)
                game_world.add_object(demon, 2)
                game_world.add_collision_pair('forager:demon', None, demon)
                game_world.add_collision_pair('forager:demon', server.forager, None)

        if self.phase == 1:
            self.x = pico2d.clamp(680, self.x, 1240)
            self.y = pico2d.clamp(260, self.y, 800)
        elif self.phase == 2:
            self.x = pico2d.clamp(680, self.x, 1800)
            self.y = pico2d.clamp(260, self.y, 800)
        elif self.phase == 3:
            self.x = pico2d.clamp(680, self.x, 1800)
            self.y = pico2d.clamp(-300, self.y, 800)


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
        self.font_coin.draw(self.font_coin.x, self.font_coin.y, f'{self.coin}', (255, 255, 255))

        if self.useItemCount == 1:
            self.image_useItemSlot.draw(self.useItemSlot_x, self.useItemSlot_y, 100, 100)
            self.image_useItem.draw(self.useItemSlot_x, self.useItemSlot_y, 100, 100)
        # elif self.useItemCount == 2:
        #     self.image_useItemSlot.draw(self.useItemSlot_x - 50, self.useItemSlot_y, 100, 100)
        #     self.image_useItemSlot.draw(self.useItemSlot_x + 50, self.useItemSlot_y, 100, 100)

    def set_item(self, item):
        self.item = item

    def get_bb(self):
        return 947, 532, 973, 552
    
    def handle_collision(self, group, other):
        if group == 'forager:treedrop':
            self.woodCount += 2
        elif group == 'forager:rockdrop':
            self.rockCount += 1
        elif group == 'forager:ironrockdrop':
            self.ironrockCount += 2
        elif group == 'forager:goldrockdrop':
            self.goldrockCount += 2
        elif group == 'forager:slime':
            if self.damage_can == True:
                self.heart -= 1
                damagescreen = DamageScreen()
                game_world.add_object(damagescreen, 5)
                self.damage_can = False
                self.damage_time = pico2d.get_time()
                self.heart_time = pico2d.get_time()
        elif group == 'forager:demon':
            if self.damage_can == True:
                self.heart -= 1
                damagescreen1 = DamageScreen()
                game_world.add_object(damagescreen1, 5)
                self.damage_can = False
                self.damage_time = pico2d.get_time()
                self.heart_time = pico2d.get_time()