import pygame
import os
from os import path


class Actor(pygame.sprite.Sprite):
    """
    is an image and a position on the surface.
    """

    def __init__(self, config, position):
        """
        :param config: values from item_config.py
        :param position: (int, int). the x and y coordinates
        """
        pygame.sprite.Sprite.__init__(self)
        self.size = config["size"]
        self.texture, self.rect = self.load_image(config)
        self.texture = pygame.transform.smoothscale(self.texture, self.size)
        self.position = position
        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, surface):
        """
        :param surface: pygame.Surface.
        """
        surface.blit(self.texture, self.position)

    def load_image(self, config):
        fullname = os.path.join('assets', 'textures',
                                config['type'], config['texture'])
        try:
            image = pygame.image.load(fullname)

        except pygame.error as message:
            print('Cannot load image:', config['texture'])
            raise SystemExit(message)

        image = image.convert()

        return image, image.get_rect()
