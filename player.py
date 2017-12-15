import cocos

from controller import Controller
from joysticks import Joysticks

from pyglet.window import key


class Player(Controller):
    """
    the player
    """
    SPEED = 500

    def __init__(self, actor):
        """
        
        :param actor:
        """
        super().__init__(actor)
        # todo: generate id?
        self.id = None
        self._last_event = None
        self.keys = {
            key.LEFT: self.move_left,
            key.RIGHT: self.move_right
        }

    def handle_event(self, event_key, pressed):
        """
        :param event_key the key that is pressed
        :param pressed if the key is down or up
        :return:
        """

        method = self.keys.get(event_key)

        if method is not None:
            method(pressed)
            return True
        return False

    def on_key_press(self, key, modifiers):
        self.handle_event(key, True)

    def on_key_release(self, key, modifiers):
        self.handle_event(key, False)

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
        return False
