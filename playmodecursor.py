import game_framework
import pico2d

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class PlayModeCursor:
    image = None

    def __init__(self):
        self.x, self.y = 960, 50
        self.frame = 0

        if PlayModeCursor.image == None:
            PlayModeCursor.image = pico2d.load_image('Sprites/Cursor1x1.png')

    def draw(self):
        frameX = int(self.frame) * 40

        self.image.clip_draw(frameX, 0, 40, 40, self.x, self.y, 120, 120)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10