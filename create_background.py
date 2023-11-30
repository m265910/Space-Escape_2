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

class Space_Move(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("real_space.png").convert()

        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = 0.1


    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        for x in range(0, SCREEN_WIDTH, SPACE_TILE):
            for y in range(0, SCREEN_HEIGHT, SPACE_TILE):
                screen.blit(self.image, (x, y))

moving_space = pygame.sprite.Group()