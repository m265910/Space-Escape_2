import pygame
from game_parameters import *
new_font = pygame.font.Font("space age.ttf", 48)
instructions_font = pygame.font.Font("data-latin.ttf", 30)
wave_1 = new_font.render("WAVE 1", True, (255, 255, 155))
wave_2 = new_font.render("WAVE 2", True, (255, 255, 155))
wave_3 = new_font.render("WAVE 3", True, (255, 255, 155))
final_wave = new_font.render("FINAL WAVE", True, (255, 255, 155))

def spawn_wave1(screen):
    name_text = new_font.render("WELCOME TO SPACE ESCAPE", True, (255, 255, 255))
    screen.blit(name_text, (SCREEN_WIDTH/2 - name_text.get_width()/2, 2*SCREEN_HEIGHT/5 - name_text.get_height()/2))
    screen.blit(wave_1, (SCREEN_WIDTH / 2 - wave_1.get_width() / 2, SCREEN_HEIGHT / 2 - wave_1.get_height() / 2))