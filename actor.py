import pygame
import os
from os import path


class Actor(pygame.sprite.DirtySprite):
    """
    is an image and a position on the surface.
    """

    def __init__(self, config, position, *args):
        """
        :param config: values from item_config.py
        :param position: (int, int). the x and y coordinates
        """
        pygame.sprite.DirtySprite.__init__(self, *args)
        self.size = config["size"]
        self.texture = self.load_image(config)
        self.image = pygame.transform.smoothscale(self.texture, self.size)
        self.rect = self.image.get_rect()
        self.position = position
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self, time):
        self.position = (self.position[0] + self.x_velocity * time, self.position[1])
        self.rect.midbottom = self.position
        self.dirty = 1

    def load_image(self, config):
        """
        :param config: item_config. includes actor type, texture (filename for image)
        and size
        :return: image and image rect
        """
        fullname = os.path.join('assets', 'textures',
                                config['type'], config['texture'])
        try:
            image = pygame.image.load(fullname)

        except pygame.error as message:
            print('Cannot load image:', config['texture'])
            raise SystemExit(message)

        image = image.convert_alpha()

        return image
