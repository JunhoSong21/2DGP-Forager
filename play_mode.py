import game_framework
import game_world
import pico2d

from forager import *

def handle_events():
    global running

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN or pico2d.SDL_KEYUP:
            forager.add_event(event)

def init():
    global running
    global forager

    running = True

    forager = Forager()
    game_world.add_object(forager, 2)

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