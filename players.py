import pygame
from game_parameters import *

PLAYER_MAX = 3
PLAYER_MIN = 0.5
# Separate classes for each player
class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.new_image = pygame.image.load("player1_new.png").convert()

        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 3, self.size[1] / 3)
        self.image = pygame.transform.scale(self.new_image, self.new_size)
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
    # Stating motion commands for player1
    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED
    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_back(self):
        self.x_speed = -1 * PLAYER_SPEED
    def move_forward(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.new_image = pygame.image.load("player2.png").convert()

        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 6, self.size[1] / 6)
        self.image = pygame.transform.scale(self.new_image, self.new_size)
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
    # Stating motion commands for player2
    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED
    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_back(self):
        self.x_speed = -1 * PLAYER_SPEED
    def move_forward(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
