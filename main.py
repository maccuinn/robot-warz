import pygame
import config
from pygame.locals import *
from actor import Actor
from player import Player
from item_config import item_types
from joysticks import Joysticks
from itertools import chain

pygame.init()
pygame.joystick.init()
joysticks = Joysticks([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())])


game_name = "Robot Warz"

gameDisplay = pygame.display.set_mode(config.screen_size)
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

players = [
    Actor(item_types["player1"], (500, 600)),
    Actor(item_types["player2"], (100, 600)),
    Actor(item_types["player3"], (250, 600)),
    Actor(item_types["player4"], (900, 600))
]
controllers = [Player(p) for p in players]
id = 0
for controller in controllers:
    controller.id = id
    id += 1

robots = [
    Actor(item_types["robot1"], (200, 300)),
    Actor(item_types["robot2"], (500, 300)),
    Actor(item_types["robot3"], (800, 500)),
]

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        handled = False
        if not joysticks.allow_event(event):
            break
        for controller in controllers:
            if controller.handle_event(event):
                handled = True
                break
        if not handled and event.type not in (
                pygame.ACTIVEEVENT,
                pygame.VIDEOEXPOSE,
                pygame.MOUSEMOTION
            ):
            print(event)

    pygame.display.update()
    #TODO: update() should be changed so only the changes are updated
    #https://www.pygame.org/docs/tut/newbieguide.html
    time = clock.tick(60)
    for actor in chain(players, robots):
        actor.draw(gameDisplay)
    for actor in chain(players, robots):
        actor.update(time)

pygame.joystick.quit()
pygame.quit()
quit()