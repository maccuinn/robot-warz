"""
Module containing GameLayer
"""
from cocos.layer import Layer
from cocos.text import Label

from actor import Actor
from player import Player
from item_config import item_types
import config
from random import randint


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
            Actor(item_types["player2"], (100, 600)),
            Actor(item_types["player3"], (250, 600)),
            Actor(item_types["player4"], (900, 600)),
        ]

        width, height = config.screen_size
        grass_distance = 50
        x_margin, y_margin, width, height = (width // 2, grass_distance, width, 960)
        self.grass = [
            [
                Actor(item_types["grass" + str(randint(1, 3))], (x, y))
                for x in range(-x_margin, width + x_margin, grass_distance)
            ]
            for y in range(-y_margin, height, grass_distance)
        ]
        from cocos.batch import BatchNode
        for grass_batch in self.grass:
            batch = BatchNode()
            for grass in grass_batch:
                grass.alpha = 0.8
                batch.add(grass)
            self.add(batch, -grass_batch[0].coord.y)

        for player in self.players:
            self.add(player, -player.coord.y)
        self.add(self.label)
        self.controllers = [Player(p) for p in self.players]

        for controller in self.controllers:
            self.add(controller)

        last_player_id = 0

        for controller in self.controllers:
            controller.id = last_player_id
            last_player_id += 1

        self.robots = [
            Actor(item_types["robot1"], (200, 300)),
            Actor(item_types["robot2"], (500, 300)),
            Actor(item_types["robot3"], (800, 500)),
        ]
        for robot in self.robots:
            self.add(robot, -robot.coord.y)
            # -robot.coord.y

        self.castle = Actor(item_types["castle1"], (500, 1000))

        self.add(self.castle, -self.castle.coord.y)

        print("Game Layer Children" + str(len(self.children)))
