import game_framework
import server
import pico2d

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Slime:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, -200
        self.frame = 0
        self.CursorOn = False

        if Slime.image == None:
            Slime.image = pico2d.load_image('Sprites/Slime.png')

    def draw(self):
        frameX = int(self.frame) * 16
        self.image.clip_draw(frameX, 0, 16, 16, self.x, self.y, 32, 32)

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
