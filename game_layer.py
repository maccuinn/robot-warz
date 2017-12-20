"""
Module containing GameLayer
"""
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.text import Label
from actor import Actor
from player import Player
from item_config import item_types


class GameLayer(Layer):
    """
    Layer that holds the gameplay (grass and player(s)/robots)
    """
    is_event_handler = True

    def __init__(self, *args):
        super().__init__()

        self.label = Label("debug")
        self.label.position = 100, 100
        self.players = [
            Actor(item_types["player1"], (500, 600), self.label),
            #Actor(item_types["player2"], (100, 600)),
            #Actor(item_types["player3"], (250, 600)),
            #Actor(item_types["player4"], (900, 600)),
        ]
        for player in self.players:
            self.add(player)
        self.add(self.label)
        self.controllers = [Player(p) for p in self.players]

        for controller in self.controllers:
            self.add(controller)

        last_player_id = 0

        for controller in self.controllers:
                controller.id = last_player_id
                last_player_id += 1

        self.robots = [
            #Actor(item_types["robot1"], (200, 300)),
            #Actor(item_types["robot2"], (500, 300)),
            #Actor(item_types["robot3"], (800, 500)),
        ]
        for robot in self.robots:
            self.add(robot)