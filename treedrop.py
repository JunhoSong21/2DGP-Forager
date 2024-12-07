import game_framework
import pico2d
import server

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 20

class TreeDrop:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.cx, self.cy = 0, 0
        self.frame = 0
        self.CursorOn = False

        if TreeDrop.image == None:
            TreeDrop.image = pico2d.load_image('Sprites/WoodDrop.png')

        self.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 24)

    def draw(self):
        frameX = int(self.frame) * 18

        self.image.clip_draw(frameX, 0, 18, 18, self.x, self.y, 54, 54)
        self.font.draw(self.x + 15, self.y - 20, f'x2', (255, 255, 255))

    def update(self):
        self.x = 1920 - server.forager.x + self.cx
        self.y = 1080 - server.forager.y + self.cy

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 20