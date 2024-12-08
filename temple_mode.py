import game_framework
import play_mode
import ending_mode
import game_world
import pico2d
import server

from starbackground import *
from templebackground import *
from forager import *
from forager_shadow import *
from backpack import *
from mouse_cursor import *
from axe import *
from playmodecursor import *
from treasurechest import *
from ekey import *
from demon import *

def handle_events():
    global running, axe, ekey, treasurechest

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN or pico2d.SDL_KEYUP:
            server.forager.add_event(event)
        if ekey.ImageOn == True and event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_e:
            treasurechest.bgm.play()
            treasurechest.open = True
            game_world.remove_object(ekey)
            game_framework.change_mode(ending_mode)
        if event.type == pico2d.SDL_MOUSEMOTION:
            server.mousecursor.x, server.mousecursor.y = event.x, 1080 - event.y

            if event.x < 960:
                server.forager.imageDir = -1
            elif event.x >= 960:
                server.forager.imageDir = 1

        if event.type == pico2d.SDL_MOUSEBUTTONDOWN and event.button == pico2d.SDL_BUTTON_LEFT:
            axe.axeRotate += 2.0
            x = random.randint(1, 3)
            if x == 1:
                axe.bgm1.play(1)
            elif x == 2:
                axe.bgm2.play(2)
            elif x == 3:
                axe.bgm3.play(3)

            for layer in game_world.world:
                for o in layer:
                    if o.CursorOn == True:
                        o.hp -= 1
                        x = random.randint(1, 2)
                        if x == 1:
                            o.bgm1.play(1)
                        elif x == 2:
                            o.bgm2.play(2)


def init():
    global running, axe, ekey, treasurechest

    running = True

    starbackground = StarBackGround()
    game_world.add_object(starbackground, 0)

    templebackground = TempleBackGround()
    game_world.add_object(templebackground, 1)

    server.mousecursor = MouseCursor()
    game_world.add_object(server.mousecursor, 5)
    server.mousecursor.size = 1

    foragershadow = ForagerShadow() # 캐릭터 그림자
    game_world.add_object(foragershadow, 2)

    backpack = BackPack() # 캐릭터 가방
    game_world.add_object(backpack, 2)

    server.forager = Forager()
    game_world.add_object(server.forager, 3)
    server.forager.coin = 0
    server.forager.phase = 3

    axe = Axe() # 캐릭터 도구
    game_world.add_object(axe, 3)

    server.inventorycursor = PlayModeCursor() # 아래 인벤토리 커서
    game_world.add_object(server.inventorycursor, 4)

    treasurechest = TreasureChest()
    game_world.add_object(treasurechest, 2)

    ekey = Ekey()
    game_world.add_object(ekey, 3)
    ekey.cx, ekey.cy = 0, 480

def finish():
    pass

def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    pico2d.clear_canvas()
    game_world.render()
    pico2d.update_canvas()

def pause():
    pass

def resume():
    pass