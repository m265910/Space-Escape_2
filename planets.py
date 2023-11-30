import pygame
import random

SLOW_SPEED = 0.2
FAST_SPEED = 0.5

class Blue_Planet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.new_image = pygame.image.load("blue_planet.png").convert()
        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 3, self.size[1] / 3)
        self.image = pygame.transform.scale(self.new_image, self.new_size)
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = random.uniform(SLOW_SPEED, FAST_SPEED)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

blue_planets = pygame.sprite.Group()


class Purple_Planet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.new_image = pygame.image.load("purple_planet.png").convert()
        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 2.3, self.size[1] / 2.3)
        self.image = pygame.transform.scale(self.new_image, self.new_size)
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = random.uniform(SLOW_SPEED, FAST_SPEED)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

purple_planets = pygame.sprite.Group()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.new_image = pygame.image.load("explosion.png").convert()
        self.size = self.new_image.get_size()
        self.new_size = (self.size[0] / 5, self.size[1] / 5)
        self.image = pygame.transform.scale(self.new_image, self.new_size)
        self.new_image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)


    def update(self):
        count = 5
        for event in pygame.event.get():
            count -= 1
            if count <= 0:
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
explosions = pygame.sprite.Group()