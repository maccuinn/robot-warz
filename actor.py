import os
from os import path
from cocos.sprite import Sprite


class Actor(Sprite):
    """
    is an image and a position on the surface.
    """

    def __init__(self, config, position, *args):
        """
        :param config: values from item_config.py
        :param position: (int, int). the x and y coordinates
        """
        texture_fullname = '/'.join(['assets', 'textures',
                                     config['type'], config['texture']])
        super().__init__(texture_fullname)
        self.size = config["size"]
        self.position = position
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self, time):
        self.position = (self.position[0] + self.x_velocity * time, self.position[1])
        self.rect.midbottom = self.position
