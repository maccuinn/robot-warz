"""
Module containing BackgoundLayer
"""
from cocos.layer import Layer
from cocos.sprite import Sprite
from os import path


class BackgroundLayer(Layer):
    """
    Layer that holds the absolute bottom background layer
    """
    def __init__(self):
        """
        Create a BackgroundLayer
        """
        super().__init__()
        self.sprite = Sprite('/'.join(["assets", "textures", "environment",
                                       "background.png"]))
        self.sprite.position = 0, 0
        self.add(self.sprite)
