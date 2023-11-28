import pygame
import random
from game_parameters import *

def draw_space(screen):
    space = pygame.image.load("real_space.png").convert()
    #space.set_colorkey((0,0,0))
    for x in range(0, SCREEN_WIDTH, SPACE_TILE):
        for y in range(0, SCREEN_HEIGHT, SPACE_TILE):
            screen.blit(space, (x, y))
    title_font = pygame.font.Font("space age.ttf", 54)
    title = title_font.render("Space Escape", True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, title.get_height()/8))