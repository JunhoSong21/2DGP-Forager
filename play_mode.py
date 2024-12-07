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
from treedrop import *
from rock import *
from goldrock import *
from ironrock import *

def handle_events():
    global running, foragershadow, axe

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
    global running, foragershadow, axe

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

    server.inventorycursor = PlayModeCursor() # 아래 인벤토리 커서
    game_world.add_object(server.inventorycursor, 4)

    tree1 = Tree() # 첫번째 나무 1번줄 시작
    game_world.add_object(tree1, 2)

    tree2 = Tree() # 두번째 나무 1번줄
    game_world.add_object(tree2, 2)
    tree2.cx = -196

    tree3 = Tree() # 세번째 나무 1번줄
    game_world.add_object(tree3, 2)
    tree3.cx = -84

    rock1 = Rock() # 첫번째 바위 1번줄 끝
    game_world.add_object(rock1, 2)

    goldrock1 = GoldRock() # 첫번째 골드바위 2번줄
    game_world.add_object(goldrock1, 2)

    ironrock1 = IronRock() # 첫번째 아이언바위 6번줄
    game_world.add_object(ironrock1, 2)

    ironrock2 = IronRock()
    game_world.add_object(ironrock2, 2)
    ironrock2.cx, ironrock2.cy = 112, 56

    rock2 = Rock()
    game_world.add_object(rock2, 2)
    rock2.cx, rock2.cy = -140, 140

    goldrock2 = GoldRock()
    game_world.add_object(goldrock2, 2)
    goldrock2.cx, goldrock2.cy = 0, 168

    tree4 = Tree()
    game_world.add_object(tree4, 2)
    tree4.cx, tree4.cy = 28, -56

    tree5 = Tree()
    game_world.add_object(tree5, 2)
    tree5.cx, tree5.cy = -28, -252

    rock3 = Rock()
    game_world.add_object(rock3, 2)
    rock3.cx, rock3.cy = -84, 0

    rock4 = Rock()
    game_world.add_object(rock4, 2)
    rock4.cx, rock4.cy = -168, -140

    ironrock3 = IronRock()
    game_world.add_object(ironrock3, 2)
    ironrock3.cx, ironrock3.cy = -224, -224

    tree6 = Tree()
    game_world.add_object(tree6, 2)
    tree6.cx, tree6.cy = 0, 0

    tree7 = Tree()
    game_world.add_object(tree7, 2)
    tree7.cx, tree7.cy = 224, -224

def finish():
    game_world.clear()

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