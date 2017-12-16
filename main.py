
from pyglet.input import get_joysticks

import config
from game_scene import GameScene

joysticks = get_joysticks()

game_name = "Robot Warz"
import patch_director
patch_director.exec()

from cocos.director import director

window = director.init(
    width=config.screen_size[0],
    height=config.screen_size[1],
    caption=game_name,
    resizable=True
)

director._usable_width = config.screen_size[0] * 2
director._usable_height = config.screen_size[1] * 2


director.show_FPS = True
print("Window config: {0}".format(window.config))

director.run(GameScene())
