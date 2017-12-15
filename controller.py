from actor import Actor
from cocos.cocosnode import CocosNode
from cocos.director import director

from pyglet.window.key import symbol_string


class Controller(CocosNode):
    """
    controls an actor
    """

    def __init__(self, actor: Actor):
        """
        :type actor: Actor
        :param actor: the actor to move
        """
        assert isinstance(actor, Actor)
        self.actor = actor
        self.visible = False

    def on_enter(self):
        """
        makes the controller an event handler
        """
        director.window.push_handlers(self)

    def on_exit(self):
        """
        removes handlers
        """
        director.window.remove_handlers(self)




