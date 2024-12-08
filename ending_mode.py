import game_framework
import game_world
import pico2d

from endingscreen import *

def handle_events():
    pass

def init():
    global running

    running = True

    endingscreen = EndingScreen()
    game_world.add_object(endingscreen, 5)

def finish():
    game_world.clear()

def update():
    game_world.update()

def draw():
    pico2d.clear_canvas()
    game_world.render()
    pico2d.update_canvas()

def pause():
    pass

def resume():
    pass