import pygame
import os

class Actor:

    def __init__(self, config, position):
        """
        :param config: values from item_config.py
        :param position: (int, int). the x and y coordinates
        """
        self.size = config["size"]
        self.texture = pygame.image.load(os.path.join("assets", "textures", config["texture"]))
        self.texture = pygame.transform.smoothscale(self.texture, self.size)
        self.position = position


    def draw(self, surface):
        """
        :param surface: pygame.Surface.
        """
        surface.blit(self.texture, self.position)


