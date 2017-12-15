import cocos
import patch_pyglet
from cocos.director import director
from pyglet.input import get_joysticks

import config
from game_scene import GameScene
from joysticks import Joysticks

import os
print(os.getcwd())
print("sdl_lib_path: {0}".format(cocos.sdl_lib_path))
print("cocos version: {0}".format(cocos.version))

joysticks = get_joysticks()

game_name = "Robot Warz"

window = director.init(
    width=config.screen_size[0],
    height=config.screen_size[1],
    caption=game_name
)
director.show_FPS = True
print("Window config: {0}".format(window.config))

director.run(GameScene())
