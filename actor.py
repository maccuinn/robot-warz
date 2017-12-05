import pygame
import os

class Actor:
    """
    is an image and a position on the surface.
    has a controller that can move it around
    """

    def __init__(self, config, position):
        """
        :param config: values from item_config.py
        :param position: (int, int). the x and y coordinates
        """
        self.size = config["size"]
        self.texture = self.load_image(config)
        self.texture = pygame.transform.smoothscale(self.texture, self.size)
        self.position = position

    def draw(self, surface):
        """
        :param surface: pygame.Surface.
        """
        surface.blit(self.texture, self.position)

    def load_image(self, config):
        fullname = os.path.join('assets', 'textures', config['texture'])
        try:
            image = pygame.image.load(fullname)

        except pygame.error as message:
            print('Cannot load image:', config['texture'])
            raise SystemExit(message)

        image = image.convert()

        return image
