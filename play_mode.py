import game_framework
import game_world
import pico2d

from mouse_cursor import *
from background import *
from forager import *
from forager_shadow import *
from grassland import *

def handle_events():
    global running, mousecursor, forager, foragershadow

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN or pico2d.SDL_KEYUP:
            forager.add_event(event)

        if event.type == pico2d.SDL_MOUSEMOTION:
            mousecursor.x, mousecursor.y = event.x, 1080 - event.y

            if event.x < 960:
                forager.imageDir = -1
            elif event.x >= 960:
                forager.imageDir = 1

def init():
    global running, mousecursor, forager, foragershadow

    running = True

    mousecursor = MouseCursor()
    game_world.add_object(mousecursor, 4)
    mousecursor.size = 1

    background = BackGround()
    game_world.add_object(background, 0)

    grassland = GrassLand()
    game_world.add_object(grassland, 1)

    forager = Forager()
    game_world.add_object(forager, 3)

    foragershadow = ForagerShadow()
    game_world.add_object(foragershadow, 2)

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