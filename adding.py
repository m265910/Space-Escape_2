import random
from game_parameters import *
from planets import Blue_Planet, Purple_Planet, blue_planets, purple_planets
from bad_guys import Bad_Ship1, bad_ships1, bad_ships2, Bad_Ship2
from lasers import lasers1, Laser, lasers2, Laser2

# Functions to add sprites to main_game
def spawn_blue(number):
    for i in range(number):
        blue_planets.add(Blue_Planet(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))
    # Add a specific number of sprites to a certain position
def spawn_purple(number):
    for i in range(number):
        purple_planets.add(Purple_Planet(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))

def spawn_bad1(number):
    for i in range(number):
        bad_ships1.add(Bad_Ship1(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))

def spawn_bad2(number):
    for i in range(number):
        bad_ships2.add(Bad_Ship2(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(1.75*SPACE_TILE, SCREEN_HEIGHT-(0.5*SPACE_TILE))))

# # Potentially add explosions upon collision
# def spawn_explosion(number, x, y):
#     for i in range(number):
#         explosions.add(Explosion(x, y))

def spawn_lasers1(number, pos, angle):
    for i in range(number):
        lasers1.add(Laser(pos[0], pos[1], angle))

def spawn_lasers2(number, pos):
    for i in range(number):
        lasers2.add(Laser2(pos[0], pos[1]))