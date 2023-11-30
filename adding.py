import pygame
import random
from game_parameters import *
from planets import Blue_Planet, Purple_Planet, blue_planets, purple_planets, Explosion, explosions
from bad_guys import Bad_Ship1, bad_ships1, bad_ships2, Bad_Ship2
from lasers import lasers1, Laser
from create_background import Space_Move, moving_space

def spawn_blue(number):
    for i in range(number):
        blue_planets.add(Blue_Planet(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))

def spawn_purple(number):
    for i in range(number):
        purple_planets.add(Purple_Planet(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))

def spawn_bad1(number):
    for i in range(number):
        bad_ships1.add(Bad_Ship1(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))

def spawn_bad2(number):
    for i in range(number):
        bad_ships2.add(Bad_Ship2(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))
def spawn_space(number):
    for i in range(number):
        moving_space.add(Space_Move(SCREEN_WIDTH, SCREEN_HEIGHT))


def spawn_explosion(number, x, y):
    for i in range(number):
        explosions.add(Explosion(x, y))

def spawn_lasers1(number,x, y, angle):
    for i in range(number):
        lasers1.add(Laser(number, x, y, angle))