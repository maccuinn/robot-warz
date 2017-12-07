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
            pygame.K_UP: self.move_forward,
            pygame.K_DOWN: self.move_back
        }
        method = move.get(event.key)

        if method is not None:
            method(event.type)

    def move_left(self, is_moving):
        """
        if keydown, move player along x coordinate
        if keyup, reset player to zero speed

        :param is_moving: bool. if event is keydown,
        is_moving will be true
        """
        if is_moving:
            self.actor.x_velocity -= Player.SPEED
        else:
            self.actor.x_velocity = 0

    def move_right(self, is_moving):
        """
        if keydown, move player along x coordinate
        if keyup, reset player to zero speed

        :param is_moving: bool. if event is keydown
        is_moving will be true
        """
        if is_moving:
            self.actor.x_velocity += Player.SPEED
        else:
            self.actor.x_velocity = 0

    def move_forward(self, is_moving):
        """
        if keydown, move player along y coordinate
        if keyup, reset player to zero speed

        :param is_moving: bool. if event is keydown
        is_moving will be true
        """
        if is_moving:
            self.actor.y_velocity += Player.SPEED
        else:
            self.actor.y_velocity = 0

    def move_back(self, is_moving):
        """
        if keydown, move player along y coordinate
        if keyup, reset player to zero speed

        :param is_moving: bool. if event is keydown
        is_moving will be true
        """
        if is_moving:
            self.actor.y_velocity -= Player.SPEED
        else:
            self.actor.y_velocity = 0

