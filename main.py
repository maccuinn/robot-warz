import pygame
import config
from pygame.locals import *
from actor import Actor
from player import Player
from item_config import item_types
from joysticks import Joysticks
from itertools import chain

pygame.init()

version = pygame.get_sdl_version()
print("sdl version: {0}.{1}.{2}".format(*version))

pygame.joystick.init()
joysticks = Joysticks([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())])

game_name = "Robot Warz"

screen = pygame.display.set_mode(config.screen_size)
print("Screen flags: {0}".format(screen.get_flags()))
print("Screen driver: {0}".format(pygame.display.get_driver()))
print("Display Info: {0}".format(pygame.display.Info()))
pygame.display.set_caption(game_name)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((208, 223, 237))

screen.blit(background, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

players = pygame.sprite.Group(
    Actor(item_types["player1"], (500, 600)),
    Actor(item_types["player2"], (100, 600)),
    Actor(item_types["player3"], (250, 600)),
    Actor(item_types["player4"], (900, 600)),
)

controllers = [Player(p) for p in players.sprites()]
last_player_id = 0

for controller in controllers:
    controller.id = last_player_id
    last_player_id += 1

robots = pygame.sprite.Group(
    Actor(item_types["robot1"], (200, 300)),
    Actor(item_types["robot2"], (500, 300)),
    Actor(item_types["robot3"], (800, 500)),
)

all_sprites = pygame.sprite.LayeredDirty(players, robots)
all_sprites.clear(screen, background)

crashed = False

while not crashed:
    time = clock.tick(60)

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

    all_sprites.update(time)
    rects = all_sprites.draw(screen)

    pygame.display.update(rects)

pygame.joystick.quit()
pygame.quit()
quit()