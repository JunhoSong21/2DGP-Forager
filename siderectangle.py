import game_world
import pico2d

class SideRectangle:
    image = None

    #1920 1080
    def __init__(self):
        self.x, self.y = 1830, 200
        self.item = None
        self.itemimage = pico2d.load_image('Sprites/Wood.png')
        self.font = pico2d.load_font('Sprites/DungGeunMo.ttf', 50)
        self.starttime = pico2d.get_time()

        if SideRectangle.image == None:
            SideRectangle.image = pico2d.load_image('Sprites/SideRectangle.png')

    def draw(self):
        self.image.draw(self.x, self.y, 180, 60)
        self.itemimage.draw(self.x - 90, self.y, 72, 72)
        self.font.draw(self.x - 40, self.y, f'Wood (2)', (255, 255, 255))

    def update(self):
        if pico2d.get_time() - self.starttime >= 3.0:
            game_world.remove_object(self)