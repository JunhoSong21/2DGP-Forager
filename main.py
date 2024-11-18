import pico2d
import game_framework
import mainmenu_mode as start_mode

pico2d.open_canvas(1920, 1080)
game_framework.run(start_mode)
pico2d.close_canvas()