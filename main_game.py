import sys
import pygame
import time
import random
from game_parameters import *
from create_background import draw_space, Space_Move
from adding import spawn_blue, spawn_purple, spawn_bad1, spawn_bad2, spawn_explosion, spawn_lasers1
from planets import purple_planets, blue_planets, Blue_Planet, Purple_Planet, explosions, Explosion
from bad_guys import Bad_Ship1, bad_ships1, Bad_Ship2, bad_ships2
from players import Player1, Player2
from math import atan2
from lasers import lasers1, Laser
# from messages import spawn_wave1

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player1_heart_new = pygame.image.load("heart.png").convert()
player1_heart_new_size = player1_heart_new.get_size()
player1_heart_new_new_size = (player1_heart_new_size[0] / 2, player1_heart_new_size[1] / 2)
player1_heart = pygame.transform.scale(player1_heart_new, player1_heart_new_new_size)
player1_heart.set_colorkey((0,0,0))

player2_heart_new = pygame.image.load("blue_heart_real.png").convert()
player2_heart_new_size = player2_heart_new.get_size()
player2_heart_new_new_size = (player2_heart_new_size[0] / 11, player2_heart_new_size[1] / 11)
player2_heart = pygame.transform.scale(player2_heart_new, player2_heart_new_new_size)
player2_heart.set_colorkey((0,0,0))

background_sound = pygame.mixer.Sound("ES_Trickster's Birthday - Chibi Power.wav")
boom_sound = pygame.mixer.Sound("explosion.wav")
hit = pygame.mixer.Sound("hurt.wav")

player1_lives = 3
player2_lives = 3
spawn_blue(3)
spawn_purple(3)
spawn_bad1(3)
spawn_bad2(3)
player1 = Player1(SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
player2 = Player2(SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/4)
game_font = pygame.font.Font("space age.ttf", 48)
instructions_font = pygame.font.Font("data-latin.ttf", 30)
wave_font = pygame.font.Font("space age.ttf", 56)
count_font = pygame.font.Font("data-latin.ttf", 48)

def spawn_welcome(screen):
    name_text = game_font.render("WELCOME TO SPACE ESCAPE", True, (255, 255, 255))
    screen.blit(name_text, (SCREEN_WIDTH/2 - name_text.get_width()/2, 2*SCREEN_HEIGHT/5 - name_text.get_height()/2))
    instructions_1 = instructions_font.render("Dodge through the galaxy by avoiding enemy spaceships", True, (155, 155, 255))
    instructions_2 = instructions_font.render("and refueling at blue planets to escape. Player 1, use", True, (155, 155, 255))
    instructions_3 = instructions_font.render("keyboard arrows to navigate, Player 2, use 'WADS'." , True, (155, 155, 255))
    instructions_4 = instructions_font.render("Outlast the waves of enemies to successfully escape.", True, (155, 155, 255))
    screen.blit(instructions_1, (SCREEN_WIDTH/2 - instructions_1.get_width()/2, SCREEN_HEIGHT*4/7 + instructions_1.get_height()/2))
    screen.blit(instructions_2, (SCREEN_WIDTH/2 - instructions_1.get_width()/2, SCREEN_HEIGHT*4/7 + 2.5*instructions_1.get_height()/2))
    screen.blit(instructions_3, (SCREEN_WIDTH/2 - instructions_1.get_width()/2, SCREEN_HEIGHT*4/7 + 4*instructions_1.get_height()/2))
    screen.blit(instructions_4, (SCREEN_WIDTH/2 - instructions_1.get_width()/2, SCREEN_HEIGHT*4/7 + 5.5*instructions_1.get_height()/2))

draw_intro = True


wave_1 = wave_font.render("WAVE 1", True, (255, 255, 155))
wave_2 = wave_font.render("WAVE 2", True, (255, 255, 155))
wave_3 = wave_font.render("WAVE 3", True, (255, 255, 155))
final_wave = wave_font.render("FINAL WAVE", True, (255, 255, 155))

def spawn_wave(screen, wave):
    screen.blit(wave, (SCREEN_WIDTH / 2 - wave.get_width() / 2, SCREEN_HEIGHT / 2 - wave.get_height() / 2))

countdown = 90
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
winning_text = game_font.render("!!YOU ESCAPED!!", True, (255, 255, 255))
losing_text = game_font.render("GAME OVER", True, (255, 255, 255))

background = screen.copy()
draw_space(background)
running = True
while running:
    pygame.mixer.Sound.play(background_sound)
    if draw_intro:
        draw_intro = False
        spawn_welcome(screen)
        pygame.display.flip()
        time.sleep(5)
        draw_wave_1 = True
    if draw_wave_1:
        draw_wave_1 = False
        screen.blit(background, (0,0))
        spawn_wave(screen, wave_1)
        pygame.display.flip()
        time.sleep(3)

    count = count_font.render(f"{countdown}", True, (255, 255, 255))
    screen.blit(count, (SPACE_TILE, SCREEN_HEIGHT - SPACE_TILE ))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player1.stop()
        player2.stop()
        # if player1_lives == 0:
        #     screen.blit(background, (0, 0))
        #     screen.blit(losing_text, (SCREEN_WIDTH / 2 - losing_text.get_width() / 2, SCREEN_HEIGHT / 2 - losing_text.get_height() / 2))
        #     pygame.display.flip()
        #     time.sleep(5)
        #     running = False
        # if player2_lives == 0:
        #     screen.blit(background, (0,0))
        #     screen.blit(losing_text, (SCREEN_WIDTH/2 - losing_text.get_width()/2 , SCREEN_HEIGHT/2 - losing_text.get_height()/2))
        #     pygame.display.flip()
        #     time.sleep(5)
        #     running = False
        if event.type == pygame.USEREVENT:
            countdown -= 1


            if countdown == 80:
                draw_wave_2 = True
                if draw_wave_2:
                    draw_wave_2 = False
                    screen.blit(background, (0,0))
                    spawn_wave(screen, wave_2)
                    pygame.display.flip()
                    BAD_MIN += 0.2
                    BAD_MAX += 0.2
                    time.sleep(2.25)
                    for bad in bad_ships1:
                        bad_ships1.remove(bad)
                        spawn_bad1(1)
                    for bad in bad_ships2:
                        bad_ships2.remove(bad)
                        spawn_bad2(1)
                    spawn_bad1(1)
                    spawn_bad2(1)


            if countdown == 70:
                draw_wave_3 = True
                if draw_wave_3:
                    draw_wave_3 = False
                    screen.blit(background, (0,0))
                    spawn_wave(screen, wave_3)
                    pygame.display.flip()
                    BAD_MIN += 0.2
                    BAD_MAX += 0.2
                    time.sleep(2.25)
                    for bad in bad_ships1:
                        bad_ships1.remove(bad)
                        spawn_bad1(1)
                    for bad in bad_ships2:
                        bad_ships2.remove(bad)
                        spawn_bad2(1)
                    spawn_bad1(1)
                    spawn_bad2(1)

            if countdown == 60:
                draw_final_wave = True
                if draw_final_wave:
                    draw_final_wave = False
                    screen.blit(background, (0, 0))
                    spawn_wave(screen, final_wave)
                    pygame.display.flip()
                    BAD_MIN += 0.2
                    BAD_MAX += 0.2
                    time.sleep(2.25)
                    for bad in bad_ships1:
                        bad_ships1.remove(bad)
                        spawn_bad1(1)
                    for bad in bad_ships2:
                        bad_ships2.remove(bad)
                        spawn_bad2(1)
                    spawn_bad1(1)
                    spawn_bad2(1)

            if countdown <= 0:
                screen.blit(background, (0,0))
                screen.blit(winning_text, (SCREEN_WIDTH/2 - winning_text.get_width()/2 , SCREEN_HEIGHT/2 - winning_text.get_height()/2 ))
                pygame.display.flip()
                time.sleep(5)
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSLASH:
                player2.move_up()

            if event.key == pygame.K_BACKSLASH:
                player2.move_down()

            if event.key == pygame.K_SPACE:
                player2.move_back()

            if event.key == pygame.K_PERIOD:
                player2.move_forward()

            if event.key == pygame.K_UP:
                player1.move_up()

            if event.key == pygame.K_DOWN:
                player1.move_down()

            if event.key == pygame.K_LEFT:
                player1.move_back()

            if event.key == pygame.K_RIGHT:
                player1.move_forward()



        # elif event.type == pygame.MOUSwwEBUTTONDOWN:
        #     if pygame.mouse.get_pressed()[0]:
        #         pos = player1.rect.midright
        #         mouse_x, mouse_y = pygame.mouse.get_pos()
        #         angle = - atan2(mouse_y - pos[1], mouse_x - pos[0])
        #         spawn_lasers1(1, pos[0], pos[1], angle)

    blue_planets.update()
    purple_planets.update()
    player1.update()
    player2.update()
    lasers1.update(player1)
    explosions.update()


    for i in bad_ships1:
        y1 = i.y - player1.y
        x1 = i.x - player1.x
        theta1 = atan2(y1, x1)
        i.update(theta1)
    for i in bad_ships2:
        y2 = i.y - player2.y
        x2 = i.x - player2.x
        theta2 = atan2(y2, x2)
        i.update(theta2)

    result_1 = pygame.sprite.spritecollide(player1, bad_ships1, True)
    result_2 = pygame.sprite.spritecollide(player2, bad_ships1, True)
    result_3 = pygame.sprite.spritecollide(player1, bad_ships2, True)
    result_4 = pygame.sprite.spritecollide(player2, bad_ships2, True)
    result_5 = pygame.sprite.spritecollide(player1, blue_planets, True)
    result_6 = pygame.sprite.spritecollide(player2, blue_planets, True)
    result_7 = pygame.sprite.spritecollide(player1, purple_planets, True)
    result_8 = pygame.sprite.spritecollide(player2, purple_planets, True)
    if result_1:
        pygame.mixer.Sound.play(hit)
        player1_lives -= 1
        spawn_bad1(1)
    if result_2:
        pygame.mixer.Sound.play(hit)
        player2_lives -= 1
        spawn_bad1(1)
    if result_3:
        pygame.mixer.Sound.play(hit)
        player1_lives -= 1
        spawn_bad2(1)
    if result_4:
        pygame.mixer.Sound.play(hit)
        player2_lives -= 1
        spawn_bad2(1)
    if result_5:
        if player1_lives < 3:
            player1_lives += 1
        spawn_blue(1)
    if result_6:
        if player2_lives < 3:
            player2_lives += 1
        spawn_blue(1)
    if result_7:
        player1_lives -= 1
        spawn_purple(1)
    if result_8:
        player2_lives -= 1
        spawn_purple(1)


    for i in lasers1:
        if i.rect.x > SCREEN_WIDTH:
            lasers1.remove(i)

        for bad1 in bad_ships1:
            bad1_hit = pygame.sprite.spritecollide(i, bad_ships1, True)
            if bad1_hit:
                bad_ships1.remove(bad1)
                lasers1.remove(i)
                spawn_bad1(1)

        for bad2 in bad_ships2:
            bad2_hit = pygame.sprite.spritecollide(i, bad_ships2, True)
            if bad2_hit:
                bad_ships2.remove(bad2)
                lasers1.remove(i)
                spawn_bad2(1)






    players = [player1, player2]
    for player in players:
        if player.rect.x < 0:
            player.rect.x = 0
        if player.rect.x > SCREEN_WIDTH - player.rect.width:
            player.rect.x = SCREEN_WIDTH - player.rect.width
        if player.rect.y < 0.25*SPACE_TILE+player1_heart.get_height():
            player.rect.y = 0.25*SPACE_TILE+player1_heart.get_height()
        if player.rect.y > SCREEN_HEIGHT - player.rect.height:
            player.rect.y = SCREEN_HEIGHT - player.rect.height


    for blue in blue_planets:
        if blue.rect.x < -blue.rect.width:
            blue_planets.remove(blue)
            spawn_blue(1)

        # for bad in bad_ships1:
        #     blue_ship = pygame.sprite.spritecollide(blue, bad_ships1, True)
        #     if blue_ship:
        #         pos = bad.rect.midright
        #         bad_ships1.remove(bad)
        #         blue_planets.remove(blue)
        #         # spawn_explosion(1, pos[0], pos[1])
        #         pygame.mixer.Sound.play(boom_sound)
        #         spawn_bad1(1)
        #         spawn_blue(1)
        #
        #     for bad in bad_ships2:
        #         blue_ship = pygame.sprite.spritecollide(blue, bad_ships2, True)
        #         if blue_ship:
        #             pos = bad.rect.midright
        #             bad_ships2.remove(bad)
        #             blue_planets.remove(blue)
        #             pygame.mixer.Sound.play(boom_sound)
        #             spawn_bad2(1)
        #             spawn_blue(1)



    for purple in purple_planets:
        if purple.rect.x < -purple.rect.width:
            purple_planets.remove(purple)
            spawn_purple(1)
    for bad in bad_ships1:
        if bad.rect.x < -bad.rect.width:
            bad_ships1.remove(bad)
            spawn_bad1(1)
    for bad in bad_ships2:
        if bad.rect.x < -bad.rect.width:
            bad_ships2.remove(bad)
            spawn_bad2(1)

    screen.blit(background, (0, 0))

    blue_planets.draw(screen)
    purple_planets.draw(screen)
    bad_ships1.draw(screen)
    bad_ships2.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    explosions.draw(screen)


    for i in lasers1:
        i.draw_laser(screen)

    for i in range(player1_lives):
        screen.blit(player1_heart, (0.5*SPACE_TILE+(i*SPACE_TILE), 0.25*SPACE_TILE))
    for i in range(player2_lives):
        screen.blit(player2_heart, (SCREEN_WIDTH - (SPACE_TILE+i*SPACE_TILE), 0.25*SPACE_TILE))

    pygame.display.flip()

pygame.quit()
sys.exit()
