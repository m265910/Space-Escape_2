import pygame
from game_parameters import *
from math import cos, sin

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.rect = pygame.Rect(0, 0, LASER_WIDTH, LASER_HEIGHT)
        self.x = x
        self.y = y
        self.angle = angle
    # Update laser 1 in direction of mouse position upon click
    def update(self, player):
        self.x += LASER_SPEED * cos(self.angle)
        self.y -= LASER_SPEED * sin(self.angle)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_laser(self, screen):
        pygame.draw.rect(screen, (215, 53, 2), self.rect)
# Create sprite group
lasers1 = pygame.sprite.Group()

class Laser2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(0, 0, LASER2_WIDTH, LASER2_HEIGHT)
        self.x = x
        self.y = y

    # Update laser 2 to move in +x direction upon pressing SPACEBAR
    def update(self, player):
        self.x += LASER_SPEED
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_laser(self, screen):
        pygame.draw.rect(screen, LASER2_COLOR, self.rect)
# Create sprite group
lasers2 = pygame.sprite.Group()