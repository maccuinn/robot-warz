import pygame
import config
from pygame.locals import *
from actor import Actor
from item_config import item_types

pygame.init()

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
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            crashed = True

    pygame.display.update()
    #TODO: update() should be changed so only the changes are updated
    #https://www.pygame.org/docs/tut/newbieguide.html

    for player in players:
        player.draw(gameDisplay)
    for robot in robots:
        robot.draw(gameDisplay)
    clock.tick(60)

pygame.quit()
quit()