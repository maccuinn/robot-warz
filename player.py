import cocos

from controller import Controller
from actor import Actor
from game_config import item_types

from pyglet.window import key

from cocos.euclid import Vector3


class Player(Controller):
    """
    the player
    """
    SPEED = 500
    SHOOT_SPEED = 1000;

    def __init__(self, actor):
        """
        :param actor: an Actor

        id: player number
        keys: Dictionary. Keys are the key commands available in the game. Values are the
            methods associated with each key press.
        """
        super().__init__(actor)
        # todo: generate id?
        self.id = None
        self.keys = {
            key.LEFT: self.move_left,
            key.RIGHT: self.move_right,
            key.UP: self.move_forward,
            key.DOWN: self.move_backward,
            key.SPACE: self.shoot,
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

    def shoot(self, key_down):
        if key_down:
            x, y = self.actor.coord.xy
            rock = Actor(item_types["rock"], (x, y, self.actor.size[1] * 0.6))
            rock.velocity = Vector3(y=Player.SHOOT_SPEED)
            rock.owner = self.actor

            game_layer = self.actor.parent
            game_layer.add(rock)
            game_layer.projectiles.append(rock)
