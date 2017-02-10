"""
    MAIN CLASS FOR 'SAVE ME RIGHT MEOW' GAME PROJECT
"""
import sys
import pygame
import constants as constants
import round as rnd
import setup_files.setup_display as display
from pygame.locals import *
from game import Game
from game_objects.wind import Wind
from characters.main_character import MainCharacter
from game_objects.food import Food


def main():
    # initialize pygame, surface, and background
    pygame.init()
    pygame.display.set_caption("Save Me Right Meow")
    FPS_CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(constants.WINDOW_SIZE)

    # display the introduction screen
    display.display_intro_screen()

    # create the main player
    player = MainCharacter()

    # create the rounds + the game
    list_of_rounds = [rnd.MainScreen(player), rnd.Round_01(player), rnd.Round_02(player), rnd.Round_03(player),
                      rnd.Round_04(player), rnd.Round_05(player), rnd.EndScreen(player)]
    game = Game(list_of_rounds, constants.GAME_TIME)

    # cue music
    sound_effect_wind = pygame.mixer.Sound(constants.SOUND_WIND)

    # font rendering (music + other)
    timer_font = pygame.font.Font(constants.FONT1, 30)
    food_left_font = pygame.font.Font(constants.FONT1, 25)
    cats_saved_font = pygame.font.Font(constants.FONT1, 25)
    music_font = pygame.font.Font(constants.FONT1, 30)
    lives_font = pygame.font.Font(constants.FONT1, 30)
    score_font = pygame.font.Font(constants.FONT1, 30)
    wind_info_font = pygame.font.Font(constants.FONT1, 25)

    # set the player's initial position for the main screen
    game.round.player.rect.x = 4 * 32
    game.round.player.rect.y = 11 * 32

    while True:  # <--- main game loop

        """ START EVENT """
        for event in pygame.event.get():
            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()

            if (not game.round.player.alive) or game.time_up:
                game.round.music.stop()
                display.display_game_over(SCREEN, game.round.player.score, game.cats_saved,
                                          game.time_left, game.round.player.lives)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                # pause screen
                if event.key == pygame.K_p:
                    if game.music_on:
                        game.round.music.set_volume(0)
                    display.display_help_screen()
                    if game.music_on:
                        game.round.music.set_volume(constants.DEFAULT_SOUND_LEVEL)
                # player movement
                if event.key == pygame.K_LEFT:
                    game.round.player.go_left()
                if event.key == pygame.K_RIGHT:
                    game.round.player.go_right()
                if event.key == pygame.K_UP:
                    game.round.player.go_up()
                if event.key == pygame.K_DOWN:
                    game.round.player.go_down()
                # player creates wind
                if event.key == pygame.K_SPACE:
                    if len(game.round.wind_list) < game.round.player.wind_ammo:
                        sound_effect_wind.play()
                        current_wind = Wind(game.round.player.rect.x, game.round.player.rect.y,
                                            game.round.player.direction, game.round.player.wind_speed)
                        game.round.add_wind(current_wind)
                # player drops food
                if event.key == pygame.K_x:
                    if game.round.player.food_inventory > 0:
                        game.round.add_food(Food(game.round.player.rect.x, game.round.player.rect.y))
                # turn music on/off
                if event.key == pygame.K_m:
                        if game.music_on:
                            game.round.music.set_volume(0)
                            game.music_on = False
                            game.music_state = "OFF"
                        else:
                            game.round.music.set_volume(constants.DEFAULT_SOUND_LEVEL)
                            game.music_on = True
                            game.music_state = "ON"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and game.round.player.change_x < 0:
                    game.round.player.stop()
                if event.key == pygame.K_RIGHT and game.round.player.change_x > 0:
                    game.round.player.stop()
                if event.key == pygame.K_UP and game.round.player.change_y < 0:
                    game.round.player.stop()
                if event.key == pygame.K_DOWN and game.round.player.change_y > 0:
                    game.round.player.stop()
        """ END EVENT """

        if game.round.player.alive and (not game.time_up):

            # update round
            game.update()
            game.draw(SCREEN)

            if game.win:
                display.display_victory_screen(SCREEN, game.round.player.score,
                                               game.cats_saved, game.time_left, game.round.player.lives)
            if game.time_up:
                game.round.music.stop()
                display.display_game_over(SCREEN, game.round.player.score, game.cats_saved,
                                          game.time_left, game.round.player.lives)

            """ ALL HEADER INFORMATION """
            if game.round_number >= 1 and (not game.win):
                SCREEN.blit(music_font.render("Music: " + game.music_state, True, constants.WHITE), [(28 * 32) + 10, 5])
                SCREEN.blit(cats_saved_font.render("Cats saved: " + str(game.cats_saved), True, constants.BLACK),
                            [(23 * 32) + 10, 5])
                SCREEN.blit(food_left_font.render("Food Left: " + str(game.round.player.food_inventory), True,
                                                  constants.BLACK), [(18 * 32) + 10, 7])
                SCREEN.blit(lives_font.render("Lives: " + str(game.round.player.lives), True, constants.BLACK),
                            [(8 * 32) + 15, 5])
                SCREEN.blit(score_font.render("Score: " + str(game.round.player.score), True, constants.BLACK),
                            [(3 * 32) + 16, 5])
                SCREEN.blit(wind_info_font.render("Ammo/Speed: " + str(game.round.player.wind_ammo) + "/" +
                                                  str(game.round.player.wind_speed)
                                                  , True, constants.BLACK), [(12 * 32) + 10, 7])

                SCREEN.blit(timer_font.render("{0:02}:{1:02}".format(game.current_minutes, game.current_seconds), True,
                                              constants.BLOOD_RED), [18, 5])
            """ END OF HEADER INFORMATION """

        pygame.display.flip()  # Update the display when all events have been processed
        FPS_CLOCK.tick(constants.FPS)


if __name__ == "__main__":
    main()
