import game_framework
import game_world
import pico2d

from mainmenubackground import MainMenuBackground
from mainmenuplay import MainMenuPlay
from mainmenulogo import MainMenuLogo
from mainmenuextras import MainMenuExtras
from mainmenuroadmap import MainMenuRoadmap
from mainmenucommunity import MainMenuCommunity
from mainmenucredits import MainMenuCredits
from mainmenuoptions import MainMenuOptions
from mainmenuexit import MainMenuExit

def handle_events():
    events = pico2d.get_events()

def init():
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