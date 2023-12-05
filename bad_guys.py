import pygame
import random
from game_parameters import *
from math import cos, sin
# Create two classes of enemies that will seek an individual player
class Bad_Ship1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.new_image = pygame.image.load("first_ship.png").convert()
        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 3, self.size[1] / 3)
        self.image = pygame.transform.scale(self.new_image, self.new_size)

        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = random.uniform(BAD_MIN, BAD_MAX)

    # Update position to move in direction of player1
    def update(self, direction):
        self.x -= self.speed * cos(direction)
        self.rect.x = self.x
        self.y -= self.speed * sin(direction)
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
# Create sprite group
bad_ships1 = pygame.sprite.Group()
class Bad_Ship2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.new_image = pygame.image.load("first_ship.png").convert()
        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 3, self.size[1] / 3)
        self.image = pygame.transform.scale(self.new_image, self.new_size)

        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = random.uniform(BAD_MIN, BAD_MAX)

    # Update position to move in direction of player2
    def update(self, direction):
        self.x -= self.speed * cos(direction)
        self.rect.x = self.x
        self.y -= self.speed * sin(direction)
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
# Create sprite group
bad_ships2 = pygame.sprite.Group()