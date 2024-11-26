import game_framework
import game_world
import pico2d

import play_mode

from mainmenubackground import MainMenuBackground
from mainmenuplay import MainMenuPlay
from mainmenulogo import MainMenuLogo
from mainmenuextras import MainMenuExtras
from mainmenuroadmap import MainMenuRoadmap
from mainmenucommunity import MainMenuCommunity
from mainmenucredits import MainMenuCredits
from mainmenuoptions import MainMenuOptions
from mainmenuexit import MainMenuExit
from mainmenucursor import MainMenuCursor

def handle_events():
    events = pico2d.get_events()
    global count

    for event in events:
        if event.type == pico2d.SDL_MOUSEMOTION:
            if count == 0 and 72 <= event.x <= 696 and 51 <= event.y <= 249:
                mainmenucursor = MainMenuCursor()
                game_world.add_object(mainmenucursor, 3)
                count += 1
            else:
                mainmenucursor.x = 2000
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_SPACE:
            game_framework.change_mode(play_mode)

def init():
    global count
    count = 0
    # MainMenuBGM = pico2d.load_wav('Sounds/Forest2.wav')
    # MainMenuBGM.set_volume(64)
    # MainMenuBGM.repeat_play()

    mainmenubackground1 = MainMenuBackground()
    game_world.add_object(mainmenubackground1, 0)

    mainmenubackground2 = MainMenuBackground()
    mainmenubackground2.x, mainmenubackground2.y = -960, 540
    game_world.add_object(mainmenubackground2, 0)

    mainmenuplay = MainMenuPlay()
    game_world.add_object(mainmenuplay, 1)

    mainmenulogo = MainMenuLogo()
    game_world.add_object(mainmenulogo, 1)

    mainmenuextras = MainMenuExtras()
    game_world.add_object(mainmenuextras, 1)

    mainmenuroadmap = MainMenuRoadmap()
    game_world.add_object(mainmenuroadmap, 1)

    mainmenucommunity = MainMenuCommunity()
    game_world.add_object(mainmenucommunity, 1)

    mainmenucredits = MainMenuCredits()
    game_world.add_object(mainmenucredits, 1)

    mainmenuoptions = MainMenuOptions()
    game_world.add_object(mainmenuoptions, 1)

    mainmenuexit = MainMenuExit()
    game_world.add_object(mainmenuexit, 1)

def update():
    game_world.update()

def draw():
    pico2d.clear_canvas()
    game_world.render()
    pico2d.update_canvas()

def finish():
    game_world.clear()

def pause():
    pass

def resume():
    pass

# 48