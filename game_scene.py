"""
Scene where all the acutal gameplay happens
"""
from cocos.scene import Scene

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

        super().__init__(*args)
