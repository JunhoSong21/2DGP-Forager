import game_framework
import game_world
import pico2d
import server
import ending_mode

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 20

class KeyDrop:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, 480
        self.frame = 0
        self.CursorOn = False

        if KeyDrop.image == None:
            KeyDrop.image = pico2d.load_image('Sprites/KeyDrop.png')
        if KeyDrop.bgm == None:
            KeyDrop.bgm = pico2d.load_wav('Sounds/ItemPickUp.wav')

    def draw(self):
        frameX = int(self.frame) * 18

        self.image.clip_draw(frameX, 0, 18, 18, self.x, self.y, 36, 36)

        pico2d.draw_rectangle(*self.get_bb())
    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 20

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
    
    def handle_collision(self, group, other):
        if group == 'forager:keydrop':
            KeyDrop.bgm.play(1)
            game_framework.change_mode(ending_mode)
            game_world.remove_object(self)   