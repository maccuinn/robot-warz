"""
Module containing BackgoundLayer
"""
from cocos.layer import Layer
from cocos.sprite import Sprite

import config


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
        width = config.screen_size[0]
        height = config.screen_size[1]
        rect = self.sprite.get_rect()
        self.sprite.image_anchor = rect.center
        self.sprite.scale_x = width / rect.width
        self.sprite.scale_y = height / rect.height

