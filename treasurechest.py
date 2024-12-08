import game_framework
import game_world
import server
import pico2d

from keydrop import *

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 9

class TreasureChest:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, 480
        self.frame = 0

        if TreasureChest.image == None:
            TreasureChest.image = pico2d.load_image('Sprites/TreasureChest.png')
        if TreasureChest.bgm == None:
            TreasureChest.bgm = pico2d.load_wav('Sounds/ChestOpen.wav')
            TreasureChest.bgm.set_volume(60)

        self.CursorOn = False
        self.open = False

    def draw(self):
        frameX = int(self.frame) * 64
        self.image.clip_draw(frameX, 0, 64, 64, self.x, self.y, 128, 128)

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        if self.open == True:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
        if int(self.frame) == 8:
            keydrop = KeyDrop()
            game_world.add_object(keydrop)
            game_world.remove_object(self)
