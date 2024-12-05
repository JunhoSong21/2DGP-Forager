import pico2d

class GrassLand:
    def __init__(self):
        self.image = pico2d.load_image('Sprites/GrassLand.png')
        self.w, self.h = self.image.w, self.image.h
        self.cw = pico2d.get_canvas_width
        self.ch = pico2d.get_canvas_height

    def draw(self):
        self.image.draw(960, 540, 560, 588)

    def update(self):
        pass
    