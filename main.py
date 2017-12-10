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

background = pygame.Surface(gameDisplay.get_size())
background = background.convert()
background.fill((208, 223, 237))

gameDisplay.blit(background, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

players = pygame.sprite.Group(
    Actor(item_types["player1"], (500, 600)),
    Actor(item_types["player2"], (100, 600)),
    Actor(item_types["player3"], (250, 600)),
    Actor(item_types["player4"], (900, 600)),
)

controllers = [Player(p) for p in players.sprites()]
id = 0

for controller in controllers:
    controller.id = id
    id += 1

robots = pygame.sprite.Group(
    Actor(item_types["robot1"], (200, 300)),
    Actor(item_types["robot2"], (500, 300)),
    Actor(item_types["robot3"], (800, 500)),
)

all_sprites = pygame.sprite.LayeredDirty(players, robots)

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

    #TODO: update() should be changed so only the changes are updated
    #https://www.pygame.org/docs/tut/newbieguide.html
    time = clock.tick(60)

    players.update(time)
    robots.update(time)

    for actor in chain(players.sprites(), robots):
        actor.draw(gameDisplay)

    pygame.display.flip()

pygame.joystick.quit()
pygame.quit()
quit()