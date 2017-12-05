import pygame
from controller import Controller


class Player(Controller):
    """
    the player
    """
    SPEED = 5

    def __init__(self):
        Controller.__init__(self)

    def handle_event(self, event):
        """
        :param event: the event to handle
        :return:
        """
        move = {
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down
        }
        method = move.get(event.key)

        if method is not None:
            method(event.type)




