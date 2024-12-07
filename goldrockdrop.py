import game_framework
import game_world
import pico2d
import server

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 20

class GoldRockDrop:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, 0
        self.frame = 0
        self.CursorOn = False

        if GoldRockDrop.image == None:
            GoldRockDrop.image = pico2d.load_image('Sprites/GoldOreDrop.png')

        if GoldRockDrop.bgm == None:
            GoldRockDrop.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 24)
            GoldRockDrop.bgm = pico2d.load_wav('Sounds/ItemPickUp.wav')
            GoldRockDrop.bgm.set_volume(32)

    def draw(self):
        frameX = int(self.frame) * 38

        self.image.clip_draw(frameX, 0, 38, 38, self.x, self.y, 76, 76)

        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 20

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    
    def handle_collision(self, group, other):
        if group == 'forager:goldrockdrop':
            GoldRockDrop.bgm.play(1)
            # siderectangle = SideRectangle()
            # siderectangle.item = 'WoodDrop'
            # game_world.add_object(siderectangle, 2)
            server.forager.coin += 1
            game_world.remove_object(self)