import pygame
from controller import Controller
from joysticks import Joysticks


class Player(Controller):
    """
    the player
    """
    S_PER_MS = 0.001
    SPEED = 500 * S_PER_MS

    def __init__(self, actor):
        super().__init__(actor)
        # todo: generate id?
        self.id = None
        self._last_event = None

    def handle_event(self, event):
        """
        :param event: the event to handle
        :return:
        """
        keys = {
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right
        }
        """
        pygame.K_UP: self.move_up,
        pygame.K_DOWN: self.move_down
        """
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            method = keys.get(event.key)

            if method is not None:
                method(event.type == pygame.KEYDOWN)
                return True
        if event.type == pygame.JOYAXISMOTION:
            return self.move_joy(event)
        return False

    def move_left(self, moving):
        self.actor.x_velocity -= Player.SPEED * (1 if moving else -1)

    def move_right(self, moving):
        self.actor.x_velocity += Player.SPEED * (1 if moving else -1)

    def move_joy(self, event):
        if event.joy == self.id:
            if event.axis == Joysticks.X_AXIS:
                if self._last_event is None or event.value != self._last_event.value:
                    self.actor.x_velocity = event.value
                return True
        return  False
