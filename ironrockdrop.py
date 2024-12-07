import game_framework
import game_world
import pico2d
import server

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 20

class IronRockDrop:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, 0
        self.frame = 0
        self.CursorOn = False

        if IronRockDrop.image == None:
            IronRockDrop.image = pico2d.load_image('Sprites/IronOreDrop.png')

        if IronRockDrop.bgm == None:
            IronRockDrop.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 24)
            IronRockDrop.bgm = pico2d.load_wav('Sounds/ItemPickUp.wav')
            IronRockDrop.bgm.set_volume(32)

    def draw(self):
        frameX = int(self.frame) * 36

        self.image.clip_draw(frameX, 0, 36, 36, self.x, self.y, 72, 72)

        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 20

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    
    def handle_collision(self, group, other):
        if group == 'forager:ironrockdrop':
            IronRockDrop.bgm.play(1)
            # siderectangle = SideRectangle()
            # siderectangle.item = 'WoodDrop'
            # game_world.add_object(siderectangle, 2)
            server.forager.coin += 3
            game_world.remove_object(self)