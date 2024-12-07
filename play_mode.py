import game_framework
import game_world
import pico2d
import server

from mouse_cursor import *
from background import *
from forager import *
from forager_shadow import *
from backpack import *
from axe import *
from grassland import *
from playmodecoin import *
from playmodecursor import *

from tree import *
from rock import *

def handle_events():
    global running, foragershadow

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN or pico2d.SDL_KEYUP:
            server.forager.add_event(event)

        if event.type == pico2d.SDL_MOUSEMOTION:
            server.mousecursor.x, server.mousecursor.y = event.x, 1080 - event.y

            if event.x < 960:
                server.forager.imageDir = -1
            elif event.x >= 960:
                server.forager.imageDir = 1

def init():
    global running, foragershadow

    running = True

    server.mousecursor = MouseCursor() #마우스 커서
    game_world.add_object(server.mousecursor, 5)
    server.mousecursor.size = 1

    background = BackGround() # 바다
    game_world.add_object(background, 0)

    grassland = GrassLand() # 땅
    game_world.add_object(grassland, 1)

    server.forager = Forager() # 캐릭터
    game_world.add_object(server.forager, 3)

    foragershadow = ForagerShadow() # 캐릭터 그림자
    game_world.add_object(foragershadow, 2)

    backpack = BackPack() # 캐릭터 가방
    game_world.add_object(backpack, 2)

    axe = Axe() # 캐릭터 도구
    game_world.add_object(axe, 4)

    tree1 = Tree() # 첫번째 나무
    game_world.add_object(tree1, 2)

    rock1 = Rock() # 첫번째 바위
    game_world.add_object(rock1, 2)

    server.inventorycursor = PlayModeCursor() # 아래 인벤토리 커서
    game_world.add_object(server.inventorycursor, 4)

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