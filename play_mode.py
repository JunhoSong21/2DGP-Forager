import game_framework
import game_world
import pico2d

from background import *
from forager import *

def handle_events():
    global running, forager

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN or pico2d.SDL_KEYUP:
            forager.add_event(event)
        elif event.type == pico2d.SDL_MOUSEMOTION:
            if event.y < 1040:
                forager.imageDir = -1
            elif event.y >= 1040:
                forager.imageDir = 1

def init():
    global running, forager

    running = True

    background = BackGround()
    game_world.add_object(background, 0)

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