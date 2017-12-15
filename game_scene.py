"""
Scene where all the acutal gameplay happens
"""
from cocos.scene import Scene
from cocos.director import director
is_cocoa = True
try:
    from pyglet.window.cocoa import CocoaWindow
except ImportError as ex:
    is_cocoa = False
from game_layer import GameLayer
from background_layer import BackgroundLayer


class GameScene(Scene):
    """
    Encapsulate the scene where the player is walking through
    a field of tall grass towards the castle and avoiding
    or shooting robots with a slingshot
    """
    def __init__(self, *args):
        args = list(args) + [BackgroundLayer(), GameLayer()]
        # hack for retina displays because pyglet fails
        # see https://github.com/los-cocos/cocos/issues/303
        # and https://bitbucket.org/pyglet/pyglet/issues/45/retina-display-scaling-on-os-x

        if is_cocoa:
            # todo: actually detect retina displays and set scale accordingly
            for layer in args:
                layer.anchor_x = 0
                layer.anchor_y = 0
                layer.scale = 2

        super().__init__(*args)
