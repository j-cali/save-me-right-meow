"""
    This module helps in setting up the displays for game events (game over, victory, introduction, pause screen).
"""
import sys

import pygame

import constants as constants


#  source: http://programarcadegames.com/python_examples/f.php?file=instruction_screen.py
def display_intro_screen():
    """ Displays the introduction screens.

    Returns:
        None
    """
    intro_screen = pygame.display.set_mode(constants.WINDOW_SIZE)
    font = pygame.font.Font(None, 36)
    special_font = pygame.font.Font(constants.FONT3, 50)
    clock = pygame.time.Clock()

    display_instructions = True
    main_page = 1
    done = False

    continue_text = font.render("Click anywhere to continue", True, constants.RED)
    instructions_bg = pygame.image.load(constants.HELP_BACKGROUND).convert()

    # -------- Intro Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_page += 1
                if main_page == 3:
                    display_instructions = False
        # Set the screen background
        intro_screen.fill(constants.BLACK)

        # story + objective
        if main_page == 1:
            text1 = font.render(constants.STORY_1, True, constants.YELLOW)
            text2 = font.render(constants.STORY_2, True, constants.WHITE)
            text3 = font.render(constants.STORY_3, True, constants.WHITE)
            text4 = font.render(constants.STORY_4, True, constants.WHITE)
            text5 = font.render(constants.STORY_5, True, constants.WHITE)
            text6 = font.render(constants.STORY_6, True, constants.WHITE)
            text7 = font.render(constants.OBJECTIVE_1, True, constants.YELLOW)
            text8 = font.render(constants.OBJECTIVE_2, True, constants.WHITE)
            text9 = font.render(constants.OBJECTIVE_3, True, constants.WHITE)
            text10 = font.render(constants.OBJECTIVE_4, True, constants.WHITE)
            text11 = font.render(constants.OBJECTIVE_5, True, constants.WHITE)
            text12 = font.render(constants.OBJECTIVE_6, True, constants.WHITE)
            text13 = font.render(constants.OBJECTIVE_7, True, constants.WHITE)
            text14 = font.render(constants.OBJECTIVE_8, True, constants.WHITE)
            text15 = font.render(constants.OBJECTIVE_9, True, constants.WHITE)

            intro_screen.blit(text1, [10, 10])
            intro_screen.blit(text2, [10, 40])
            intro_screen.blit(text3, [10, 70])
            intro_screen.blit(text4, [10, 100])
            intro_screen.blit(text5, [10, 130])
            intro_screen.blit(text6, [10, 160])
            intro_screen.blit(text7, [10, 270])
            intro_screen.blit(text8, [10, 300])
            intro_screen.blit(text9, [10, 330])
            intro_screen.blit(text10, [10, 360])
            intro_screen.blit(text11, [10, 390])
            intro_screen.blit(text12, [10, 420])
            intro_screen.blit(text13, [10, 450])
            intro_screen.blit(text14, [10, 480])
            intro_screen.blit(text15, [10, 510])

        # instructions
        if main_page == 2:
            intro_screen.blit(instructions_bg, [0, 0])
            text1 = font.render(constants.INSTRUCTION_1, True, constants.BLACK)
            text2 = font.render(constants.INSTRUCTION_2, True, constants.BLACK)
            text3 = font.render(constants.INSTRUCTION_3, True, constants.BLACK)
            text4 = font.render(constants.INSTRUCTION_4, True, constants.BLACK)
            text5 = font.render(constants.INSTRUCTION_5, True, constants.BLACK)
            text5_1 = font.render(constants.INSTRUCTION_5_1, True, constants.BLOOD_RED)
            text6 = font.render(constants.INSTRUCTION_6, True, constants.BLACK)
            text7 = special_font.render(constants.INSTRUCTION_7, True, constants.GREEN)

            intro_screen.blit(text1, [80, 140])
            intro_screen.blit(text2, [80, 190])
            intro_screen.blit(text3, [80, 260])
            intro_screen.blit(text4, [110, 330])
            intro_screen.blit(text5, [120, 390])
            intro_screen.blit(text5_1, [110, 420])
            intro_screen.blit(text6, [110, 490])
            intro_screen.blit(text7, [constants.SCREEN_WIDTH // 4, 40])

        # update all
        intro_screen.blit(continue_text, [constants.SCREEN_WIDTH // 3, 580])
        clock.tick(60)
        pygame.display.flip()


def display_game_over(screen, final_score, cats_saved, time_left, lives):
    """ Displays the game over text.

    Arguments:
        screen: the screen to draw the text into.
        final_score: the final score the player had.
        cats_saved: the number of cats the player saved.
        time_left: the time left remaining in the game.
        lives: the number of lives the player had.
    Returns:
        None
    """
    current_minutes = time_left // 60
    current_seconds = time_left % 60
    font = pygame.font.Font(None, 36)
    special_font1 = pygame.font.Font(constants.FONT1, 200)
    special_font2 = pygame.font.Font(constants.FONT3, 40)
    screen.fill(constants.BLACK)
    text1 = font.render("Time Left: {0:02}:{1:02}".format(current_minutes, current_seconds) +
                        " (" + str(time_left) + " seconds)", True, constants.YELLOW)
    text2 = font.render("Cats Saved: " + str(cats_saved), True, constants.YELLOW)
    text3 = font.render("Lives Left: " + str(lives), True, constants.YELLOW)
    text4 = font.render("Total Score: " + str(final_score), True, constants.YELLOW)
    text5 = font.render("Click anywhere to exit", True, constants.RED)
    text6 = special_font1.render("GAME OVER", True, constants.WHITE)
    text7 = special_font2.render("CATch you later!!!", True, constants.ORANGE)
    screen.blit(text1, [10, 10])
    screen.blit(text2, [10, 40])
    screen.blit(text3, [10, 70])
    screen.blit(text4, [10, 100])
    screen.blit(text5, [(constants.SCREEN_WIDTH // 3) + 50, constants.SCREEN_HEIGHT - 50])
    screen.blit(text6, [constants.SCREEN_WIDTH // 9, (constants.SCREEN_HEIGHT // 3) + 30])
    screen.blit(text7, [(constants.SCREEN_WIDTH // 3) + 50, (constants.SCREEN_HEIGHT // 2) + 100])


def display_victory_screen(screen, total_score, cats_saved, time_left, lives):
    """ Displays the the victory screen.

    Arguments:
        screen: the screen to draw the text into.
        total_score: the total score the player had.
        cats_saved: the number of cats the player saved.
        time_left: the time left remaining in the game.
        lives: the number of lives the player had.
    Returns:
        None
    """
    current_minutes = time_left // 60
    current_seconds = time_left % 60
    final_score = total_score + time_left + cats_saved + lives
    font = pygame.font.Font(None, 40)
    special_font = pygame.font.Font(constants.FONT1, 70)
    text1 = font.render("+ Time Left: {0:02}:{1:02}".format(current_minutes, current_seconds) +
                        " (" + str(time_left) + " seconds)" + " =>", True,
                        constants.WHITE)
    text2 = font.render("+ Cats Saved: " + str(cats_saved) + " =>", True, constants.WHITE)
    text3 = font.render("+ Lives Left: " + str(lives) + " =>", True, constants.WHITE)
    text4 = font.render("+ Total Score: " + str(total_score) + " =>", True, constants.WHITE)
    text5 = special_font.render("Final Score : " + str(final_score), True, constants.YELLOW)
    screen.blit(text1, [10, 10])
    screen.blit(text2, [10, 50])
    screen.blit(text3, [10, 90])
    screen.blit(text4, [10, 130])
    screen.blit(text5, [constants.SCREEN_WIDTH // 3, 50])


def display_help_screen():
    """ Displays a 'pause' screen or help screen.

    Returns:
        None
    """
    pause_screen = pygame.display.set_mode(constants.WINDOW_SIZE)
    font = pygame.font.Font(None, 36)
    special_font = pygame.font.Font(constants.FONT2, 80)
    clock = pygame.time.Clock()
    paused = True
    instructions_bg = pygame.image.load(constants.HELP_BACKGROUND).convert()

    # -------- Pause Loop -----------
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                paused = False
                break

        # instructions
        pause_screen.blit(instructions_bg, [0, 0])
        text1 = font.render(constants.INSTRUCTION_1, True, constants.BLACK)
        text2 = font.render(constants.INSTRUCTION_2, True, constants.BLACK)
        text3 = font.render(constants.INSTRUCTION_3, True, constants.BLACK)
        text4 = font.render(constants.INSTRUCTION_4, True, constants.BLACK)
        text5 = font.render(constants.INSTRUCTION_5, True, constants.BLACK)
        text5_1 = font.render(constants.INSTRUCTION_5_1, True, constants.BLOOD_RED)
        text6 = font.render(constants.INSTRUCTION_6, True, constants.BLACK)
        text7 = special_font.render("Game Paused", True, constants.BLOOD_RED)
        text8 = font.render("Click anywhere to go back", True, constants.RED)

        pause_screen.blit(text1, [80, 140])
        pause_screen.blit(text2, [80, 190])
        pause_screen.blit(text3, [80, 260])
        pause_screen.blit(text4, [110, 330])
        pause_screen.blit(text5, [120, 390])
        pause_screen.blit(text5_1, [110, 420])
        pause_screen.blit(text6, [110, 490])
        pause_screen.blit(text7, [constants.SCREEN_WIDTH // 3, 40])
        pause_screen.blit(text8, [constants.SCREEN_WIDTH // 3, 580])
        clock.tick(60)
        pygame.display.flip()
