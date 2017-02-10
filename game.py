"""
    This module is used to define a game.
"""
import pygame

import constants as constants


class Game:
    """ A game object that represents one whole game for 'Save Me Right Meow'.

    Attributes:
        win (bool): True if the player won the game, False otherwise.
        time_up (bool): True if the time is up, False otherwise.
        cats_saved (int): the number of cats the player has saved.
        rounds_list (list): a list of rounds for this game.
        round_number (int): the current round number for this game.
        round (Round): the current round for this game.
        total_time (int): total time of this game in seconds.
        time_left (int): the time left remaining for this game.
        count (int): the count to calculate the time_left.
        current_minutes (int): current minutes for this game.
        current_seconds (int): current seconds for this game.
        music_on (bool): True if the music is on, False otherwise.
    """

    win = False
    time_up = False
    cats_saved = 0

    def __init__(self, list_of_rounds, time):
        """ Initialize Game.

        Arguments:
            list_of_rounds (list): list of rounds.
            time (int): time in seconds.
        """

        # round information
        self.rounds_list = list_of_rounds
        self.round_number = 0
        self.round = self.rounds_list[self.round_number]

        # time information
        self.total_time = time
        self.time_left = time
        self.count = 0
        self.current_minutes = 0
        self.current_seconds = 0

        # music information
        self.music_on = True
        self.music_state = "ON"

        # set the player this round + play the round's music
        self.round.player.current_round = self.round
        self.round.music.play(-1)

    def round_passed(self):
        """ Returns if the round has been passed.

        Returns:
            bool: True if the player has passed this round, False if not.
        """
        satisfy_x = self.round.exit_coordinates[0] + 32 >= self.round.player.rect.x >= self.round.exit_coordinates[0]
        satisfy_y = self.round.exit_coordinates[1] <= self.round.player.rect.y <= self.round.exit_coordinates[1] + 12

        return satisfy_x and satisfy_y

    def go_next_round(self):
        """ Goes to the next round.

        Returns:
            None
        """
        self.round.music.stop()
        self.round_number += 1

        if 1 < self.round_number <= 5:
            self.round.player.lives += 1
            self.total_time += 30

        self.round = self.rounds_list[self.round_number]
        self.round.player.current_round = self.round
        self.round.player.rect.x = self.round.entrance_coordinates[0]
        self.round.player.rect.y = self.round.entrance_coordinates[1]

        if not self.music_on:
            self.round.music.play(-1)
            self.round.music.set_volume(0)
        else:
            self.round.music.play(-1)



    def update(self):
        """ Update everything in the game.

        Returns:
            None
        """
        if self.time_left <= 0:
            self.time_up = True
            self.round.player.alive = False

        if not self.time_up and not self.win:
            self.time_left = self.total_time - (self.count // constants.FPS)
            self.current_minutes = self.time_left // 60
            self.current_seconds = self.time_left % 60
            self.count += 1

        if not self.round.boss_alive and not self.win:
            self.win = True
            pygame.time.delay(3000)
            self.go_next_round()

        for c in self.round.cat_list:
            collide_with_food = pygame.sprite.spritecollideany(c, self.round.food_list)
            collide_with_food = pygame.sprite.spritecollideany(c, self.round.food_list)
            if collide_with_food is not None:
                self.cats_saved += 1

        if self.round_passed():
            self.go_next_round()

        self.round.update()

    def draw(self, screen):
        """ Draw everything in the game.

        Arguments:
            screen: the screen to draw onto
        Returns:
            None
        """
        self.round.draw(screen)
