import game_framework
import game_world
import pico2d

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class MainMenuCursor:
    image = None

    def __init__(self):
        self.x, self.y = 384, 930
        self.frame = 0
        self.size = 0
        if MainMenuCursor.image == None:
            MainMenuCursor.image = pico2d.load_image('Sprites/Cursor1x1.png')

    def draw(self):
        if self.size == 0:
            self.image.clip_draw(
                int(self.frame) * 40, 0, 20, 40, self.x - 270, self.y, 120, 240)
            self.image.clip_draw(
                int(self.frame) * 40 + 20, 0, 20, 40, self.x + 270, self.y, 120, 240)
        elif self.size == 1:
            self.image.clip_draw(
                int(self.frame) * 40, 0, 20, 40, self.x - 270, self.y, 100, 200)
            self.image.clip_draw(
                int(self.frame) * 40 + 20, 0, 20, 40, self.x + 270, self.y, 100, 200)
        elif self.size == 2:
            self.image.clip_draw(
                int(self.frame) * 40, 0, 20, 40, self.x - 230, self.y, 100, 200)
            self.image.clip_draw(
                int(self.frame) * 40 + 20, 0, 20, 40, self.x + 230, self.y, 100, 200)
        elif self.size == 3:
            pass
        elif self.size == 4:
            pass


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10