import pygame
import pygame.mixer
from game_parameters import *
pygame.mixer.init()
background_sound = pygame.mixer.Sound("ES_Trickster's Birthday - Chibi Power.wav")
# Import background music to make part of background
def draw_space(screen):
    # Make space background with music
    space = pygame.image.load("real_space.png").convert()
    pygame.mixer.Sound.play(background_sound)
    for x in range(0, SCREEN_WIDTH, SPACE_TILE):
        for y in range(0, SCREEN_HEIGHT, SPACE_TILE):
            screen.blit(space, (x, y))
    title_font = pygame.font.Font("space age.ttf", 54)
    title = title_font.render("Space Escape", True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, title.get_height()/8))
