import cocos

from controller import Controller
from joysticks import Joysticks

from pyglet.window import key

from cocos.euclid import Vector3


class Player(Controller):
    """
    the player
    """
    SPEED = 500

    def __init__(self, actor):
        """
        :param actor: an Actor
        """
        super().__init__(actor)
        # todo: generate id?
        self.id = None
        self._last_event = None
        self.keys = {
            key.LEFT: self.move_left,
            key.RIGHT: self.move_right,
            key.UP: self.move_forward,
            key.DOWN: self.move_backward
        }

    def handle_event(self, event_key, pressed):
        """
        :param event_key the key that is pressed
        :param pressed if the key is down or up
        :return: True if valid event, False if not
        """

        method = self.keys.get(event_key)

        if method is not None:
            method(pressed)
            return True
        return False

    def on_key_press(self, key, modifiers):
        return self.handle_event(key, True)

    def on_key_release(self, key, modifiers):
        return self.handle_event(key, False)

    def move_left(self, moving):
        self.actor.velocity = self.actor.velocity - Vector3(Player.SPEED * (1 if moving else -1))

    def move_right(self, moving):
        self.actor.velocity = self.actor.velocity + Vector3(Player.SPEED * (1 if moving else -1))

    def move_forward(self, moving):
        self.actor.velocity = self.actor.velocity + Vector3(y=Player.SPEED * (1 if moving else -1))

    def move_backward(self, moving):
        self.actor.velocity = self.actor.velocity - Vector3(y=Player.SPEED * (1 if moving else -1))

