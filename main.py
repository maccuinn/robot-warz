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

boy = Actor(item_types["boy"], (500, 600))

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

    boy.draw(gameDisplay)
    clock.tick(60)

pygame.quit()
quit()