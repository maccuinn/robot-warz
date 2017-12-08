"""
Let's  wrangle us some joysticks
"""
import pygame

class Joysticks:
    """
    All the joysticks you could want
    """
    DEAD_ZONE = 0.5
    X_AXIS = 0
    Y_AXIS = 1
    Z_AXIS = 2

    def __init__(self, joysticks):
        self.joysticks = joysticks
        for joystick in joysticks:
            joystick.init()

    def allow_event(self, event):
        if event.type == pygame.JOYAXISMOTION:
            if abs(event.value) < Joysticks.DEAD_ZONE:
                event.value = 0
        return True