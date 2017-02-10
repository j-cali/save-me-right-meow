"""
    This module is used to define rounds.
"""
import pygame

import constants as constants
import setup_files.setup_main_screen as main_screen
import setup_files.setup_round1 as round1
import setup_files.setup_round2 as round2
import setup_files.setup_round3 as round3
import setup_files.setup_round4 as round4
import setup_files.setup_round5 as round5
from characters.cat import NyanCat
from characters.enemy import Boss


class Round:
    """ A generic super class to define a round.

    Attributes:
        background (Surface): the background for this game.
        boss_alive (bool): True if the boss is alive, False otherwise.
        music (None): the music for this round
        entrances_coordinates (list): the x and y coordinates for the entrance for this game.
        exit_coordinates (list): the x and y coordinates for the exit for this game.
        num_of_cats (int): the number of cats for this round.
        num_of_enemies (int): the number of enemies for this round.
        num_of_obstacles (int): the number of obstacles for this round.
        round_number (int): the round number for this round.
        player (Sprite): the player for this round.
        wall_list (pygame.sprite.Group()): the list of wall sprites for this round.
        obstacle_list (pygame.sprite.Group()): the list of obstacle sprites for this round.
        enemy_list (pygame.sprite.Group()): the list of enemy sprites for this round.
        wind_list (pygame.sprite.Group()): the list of wind sprites for this round.
        cat_list (pygame.sprite.Group()): the list of cat sprites for this round.
        food_list (pygame.sprite.Group()): the list of food sprites for this round.
    """

    background = None
    boss_alive = True
    music = None
    entrances_coordinates = None
    exit_coordinates = None
    num_of_cats = None
    num_of_enemies = None
    num_of_obstacles = None
    round_number = None

    def __init__(self, player):
        """ Initialize Round.

        Arguments:
            player (Sprite): the player for this round.
        """
        self.player = player

        # Lists of sprites used in all rounds."""
        self.wall_list = pygame.sprite.Group()
        self.obstacle_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.wind_list = pygame.sprite.Group()
        self.cat_list = pygame.sprite.Group()
        self.food_list = pygame.sprite.Group()

    def update(self):
        """ Update everything in this round.

        Returns:
            None
        """
        for w in self.wind_list:
            # to prevent wind from going out of bounds
            if w.rect.x >= constants.SCREEN_WIDTH - 32 or w.rect.x <= 0\
                    or w.rect.y <= 0 or w.rect.y >= constants.SCREEN_HEIGHT - 32:
                self.wind_list.remove(w)
                break

            # remove wind if an enemy or an obstacle is hit by it
            curr_enemy = pygame.sprite.spritecollideany(w, self.enemy_list)
            curr_obs = pygame.sprite.spritecollideany(w, self.obstacle_list)
            if curr_enemy is not None:
                curr_enemy.decrease_lives()
                self.wind_list.remove(w)
                if curr_enemy.lives == 0:
                    self.enemy_list.remove(curr_enemy)
                    self.wind_list.remove(w)
                    self.player.increase_score(curr_enemy.SCORE_VALUE)
                    self.player.increase_food()
                    break
            elif curr_obs is not None:
                self.obstacle_list.remove(curr_obs)
                self.wind_list.remove(w)
                self.player.increase_wind_speed()
                break

        # increase enemy speed if they eat the food, remove the food accordingly
        for e in self.enemy_list:
            collide_with_food = pygame.sprite.spritecollideany(e, self.food_list)
            if collide_with_food is not None:
                self.food_list.remove(collide_with_food)
                e.increase_speed()

        # remove the cat if they eat the food, remove the food accordingly
        for c in self.cat_list:
            collide_with_food = pygame.sprite.spritecollideany(c, self.food_list)
            if collide_with_food is not None:
                self.food_list.remove(collide_with_food)
                self.cat_list.remove(c)
                self.player.increase_score(c.SCORE_VALUE)
                self.player.increase_max_wind()

        # update the sprites
        self.wall_list.update()
        self.obstacle_list.update()
        self.enemy_list.update()
        self.cat_list.update()
        self.wind_list.update()
        self.food_list.update()
        self.player.update()

    def draw(self, screen):
        """ Draw everything in this round.

        Arguments:
            screen: the screen to draw onto
        Returns:
            None
        """

        # draw the background
        screen.blit(self.background, [0, 0])

        # draw the sprites
        self.wall_list.draw(screen)
        self.obstacle_list.draw(screen)
        self.enemy_list.draw(screen)
        self.cat_list.draw(screen)
        self.wind_list.draw(screen)
        self.food_list.draw(screen)
        self.player.draw(screen)

    def add_wind(self, wind):
        """ Add a wind to the wind list.

        Arguments:
            wind: a wind sprite.
        Returns:
            None: adds a wind to the wind list.
        """
        self.wind_list.add(wind)

    def add_food(self, food):
        """ Add a food item to the food list.

        Arguments:
            food: a food sprite.
        Returns:
            None: adds a food item to the food list.
        """
        self.food_list.add(food)
        self.player.decrease_food()

# END OF GENERIC CLASS


"""
    Round 1 Class
        I will write all the documentation for Round_01 but will omit most documentation for Round's 2-5
        since they are similar.
"""


# Round 1
class Round_01(Round):
    """ Round 1 Definition."""

    def __init__(self, player):
        """ Initialize Round_01.

        Arguments:
            player (Sprite): the player for this round.
        """

        # Call the parent constructor
        Round.__init__(self, player)

        # Set the round number
        self.round_number = 1

        # Set the number of cats, enemies, and obstacles
        self.num_of_cats = 5
        self.num_of_enemies = 20
        self.num_of_obstacles = 50

        # entrance coordinates in this round
        self.entrance_coordinates = [1 * 32, 2 * 32]

        # put the player in the entrance coordinates
        self.player.rect.x = self.entrance_coordinates[0] - 32
        self.player.rect.y = self.entrance_coordinates[1]

        # exit coordinates to go to the next round
        self.exit_coordinates = [29 * 32, 2 * 32]

        # Set background for Round 1
        self.background = pygame.image.load(constants.BACKGROUND_ROUND1).convert()

        # Set the music for Round 1
        self.music = pygame.mixer.Sound(constants.MUSIC_ROUND1)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        # add the borders (the walls and tent) + add obstacles as a border
        round1.add_outer_walls(self.wall_list)
        round1.add_inner_walls(self.wall_list)
        round1.add_invisible_blocks(self.wall_list, self.entrance_coordinates)

        # add the enemies, obstacles, and the timer to the border list
        self.enemy_list = round1.generate_enemies(self.wall_list, self.num_of_enemies, self.player)
        self.cat_list = round1.generate_cats(self.wall_list, self.num_of_cats, self.player)
        self.obstacle_list = round1.generate_obstacles(self.wall_list, self.num_of_obstacles, self.player)

        # set up the borders so the enemies, cats, and player can stay within game (collision handling)
        for e in self.enemy_list:
            e.walls = self.wall_list
            e.obstacles = self.obstacle_list
            e.cats = self.cat_list
            e.enemies = self.enemy_list

        for c in self.cat_list:
            c.walls = self.wall_list
            c.obstacles = self.obstacle_list
            c.enemies = self.enemy_list
            c.cats = self.cat_list


# Round 2
class Round_02(Round):
    """ Definition for Round 2. """

    def __init__(self, player):
        """ Create round 2. """

        Round.__init__(self, player)

        self.round_number = 2

        self.num_of_cats = 5
        self.num_of_enemies = 25
        self.num_of_obstacles = 40

        self.entrance_coordinates = [29 * 32, 2 * 32]
        self.player.rect.x = self.entrance_coordinates[0]
        self.player.rect.y = self.entrance_coordinates[1]
        self.exit_coordinates = [2 * 32, 14 * 32]

        self.background = pygame.image.load(constants.BACKGROUND_ROUND2).convert()
        self.music = pygame.mixer.Sound(constants.MUSIC_ROUND2)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        round2.add_outer_walls(self.wall_list)
        round2.add_inner_walls(self.wall_list)
        round2.add_invisible_blocks(self.wall_list, self.entrance_coordinates)

        self.enemy_list = round2.generate_enemies(self.wall_list, self.num_of_enemies, self.player)
        self.cat_list = round2.generate_cats(self.wall_list, self.num_of_cats, self.player)
        self.obstacle_list = round2.generate_obstacles(self.wall_list, self.num_of_obstacles, self.player)

        for e in self.enemy_list:
            e.walls = self.wall_list
            e.obstacles = self.obstacle_list
            e.cats = self.cat_list
            e.enemies = self.enemy_list

        for c in self.cat_list:
            c.walls = self.wall_list
            c.obstacles = self.obstacle_list
            c.enemies = self.enemy_list
            c.cats = self.cat_list


# Round 3
class Round_03(Round):
    """ Definition for Round 3. """

    def __init__(self, player):
        """ Create round 3. """

        Round.__init__(self, player)

        self.round_number = 3

        self.num_of_cats = 5
        self.num_of_enemies = 30
        self.num_of_obstacles = 50

        self.entrance_coordinates = [1 * 32, 18 * 32]
        self.player.rect.x = self.entrance_coordinates[0]
        self.player.rect.y = self.entrance_coordinates[1]
        self.exit_coordinates = [2 * 32, 4 * 32]

        self.background = pygame.image.load(constants.BACKGROUND_ROUND3).convert()
        self.music = pygame.mixer.Sound(constants.MUSIC_ROUND3)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        round3.add_outer_walls(self.wall_list)
        round3.add_inner_walls(self.wall_list)
        round3.add_invisible_blocks(self.wall_list, self.entrance_coordinates)

        self.enemy_list = round3.generate_enemies(self.wall_list, self.num_of_enemies, self.player)
        self.cat_list = round3.generate_cats(self.wall_list, self.num_of_cats, self.player)
        self.obstacle_list = round3.generate_obstacles(self.wall_list, self.num_of_obstacles, self.player)

        for e in self.enemy_list:
            e.walls = self.wall_list
            e.obstacles = self.obstacle_list
            e.cats = self.cat_list
            e.enemies = self.enemy_list

        for c in self.cat_list:
            c.walls = self.wall_list
            c.obstacles = self.obstacle_list
            c.enemies = self.enemy_list
            c.cats = self.cat_list


# Round 4
class Round_04(Round):
    """ Definition for Round 4. """

    def __init__(self, player):
        """ Create round 4. """

        Round.__init__(self, player)

        self.round_number = 4

        self.num_of_cats = 5
        self.num_of_enemies = 25
        self.num_of_obstacles = 50

        self.entrance_coordinates = [1 * 32, 2 * 32]
        self.player.rect.x = self.entrance_coordinates[0]
        self.player.rect.y = self.entrance_coordinates[1]
        self.exit_coordinates = [29 * 32, 16 * 32]

        self.background = pygame.image.load(constants.BACKGROUND_ROUND4).convert()
        self.music = pygame.mixer.Sound(constants.MUSIC_ROUND4)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        round4.add_outer_walls(self.wall_list)
        round4.add_inner_walls(self.wall_list)
        round4.add_invisible_blocks(self.wall_list, self.entrance_coordinates)

        self.enemy_list = round4.generate_enemies(self.wall_list, self.num_of_enemies, self.player)
        self.cat_list = round4.generate_cats(self.wall_list, self.num_of_cats, self.player)
        self.obstacle_list = round4.generate_obstacles(self.wall_list, self.num_of_obstacles, self.player)

        for e in self.enemy_list:
            e.walls = self.wall_list
            e.obstacles = self.obstacle_list
            e.cats = self.cat_list
            e.enemies = self.enemy_list

        for c in self.cat_list:
            c.walls = self.wall_list
            c.obstacles = self.obstacle_list
            c.enemies = self.enemy_list
            c.cats = self.cat_list


# Round 5
class Round_05(Round):
    """ Definition for Round 5. """

    NUM_OF_CATS = 10
    NUM_OF_ENEMIES = 7
    NUM_OF_OBSTACLES = 0

    def __init__(self, player):
        """ Create round 5. """

        Round.__init__(self, player)

        self.round_number = 5

        self.entrance_coordinates = [1 * 32, 2 * 32]
        self.player.rect.x = self.entrance_coordinates[0]
        self.player.rect.y = self.entrance_coordinates[1]
        self.exit_coordinates = [30 * 32, 18 * 32]

        self.background = pygame.image.load(constants.BACKGROUND_ROUND5).convert()
        self.music = pygame.mixer.Sound(constants.MUSIC_ROUND5)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        round5.add_outer_walls(self.wall_list)
        round5.add_invisible_blocks(self.wall_list, self.entrance_coordinates)

        self.enemy_list = round5.generate_enemies(self.wall_list, self.NUM_OF_ENEMIES, self.player)
        self.cat_list = round5.generate_cats(self.wall_list, self.NUM_OF_CATS, self.player)
        self.obstacle_list = round5.generate_obstacles(self.wall_list, self.NUM_OF_OBSTACLES, self.player)

        for e in self.enemy_list:
            e.walls = self.wall_list
            e.obstacles = self.obstacle_list
            e.cats = self.cat_list
            e.enemies = self.enemy_list

        for c in self.cat_list:
            c.walls = self.wall_list
            c.obstacles = self.obstacle_list
            c.enemies = self.enemy_list
            c.cats = self.cat_list

    def update(self):
        # if the enemies are defeated, add the boss
        if len(self.enemy_list) == 0 and self.boss_alive:
            boss = Boss(500, 200)
            boss.walls = self.wall_list
            boss.cats = self.cat_list
            self.enemy_list.add(boss)

        for w in self.wind_list:
            # to prevent wind from going out of bounds
            if w.rect.x >= constants.SCREEN_WIDTH - 32 or w.rect.x <= 0\
                    or w.rect.y <= 0 or w.rect.y >= constants.SCREEN_HEIGHT - 32:
                self.wind_list.remove(w)
                break

            # remove wind if an enemy or an obstacle is hit by it
            curr_enemy = pygame.sprite.spritecollideany(w, self.enemy_list)
            curr_obs = pygame.sprite.spritecollideany(w, self.obstacle_list)
            if curr_enemy is not None:
                curr_enemy.decrease_lives()
                self.wind_list.remove(w)
                if type(curr_enemy) is Boss and curr_enemy.lives == 0:
                    self.boss_alive = False

                if curr_enemy.lives == 0:
                    self.enemy_list.remove(curr_enemy)
                    self.wind_list.remove(w)
                    self.player.increase_score(curr_enemy.SCORE_VALUE)
                    self.player.increase_food()
                    break
            if curr_obs is not None:
                self.obstacle_list.remove(curr_obs)
                self.wind_list.remove(w)
                self.player.increase_wind_speed()
                break

        for e in self.enemy_list:
            collide_with_food = pygame.sprite.spritecollideany(e, self.food_list)
            if collide_with_food is not None:
                self.food_list.remove(collide_with_food)
                e.increase_speed()

        for c in self.cat_list:
            collide_with_food = pygame.sprite.spritecollideany(c, self.food_list)
            if collide_with_food is not None:
                self.food_list.remove(collide_with_food)
                self.cat_list.remove(c)
                self.player.increase_score(c.SCORE_VALUE)
                self.player.increase_max_wind()

        self.wall_list.update()
        self.enemy_list.update()
        self.wind_list.update()
        self.food_list.update()
        self.cat_list.update()
        self.player.update()


# Main Screen
class MainScreen(Round):
    """ The main screen for this game."""

    def __init__(self, player):
        Round.__init__(self, player)

        self.round_number = 0

        self.num_of_cats = 30

        self.entrance_coordinates = [4 * 32, 12 * 32]
        self.player.rect.x = self.entrance_coordinates[0]
        self.player.rect.y = self.entrance_coordinates[1]
        self.exit_coordinates = [31 * 32, 11 * 32]

        self.background = pygame.image.load(constants.BACKGROUND_MAIN_SCREEN).convert()
        self.music = pygame.mixer.Sound(constants.MUSIC_MAIN)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        main_screen.add_outer_walls(self.wall_list)
        main_screen.add_inner_walls(self.wall_list)
        main_screen.add_invisible_blocks(self.wall_list)

        self.cat_list = main_screen.generate_cats(self.wall_list, self.num_of_cats, self.player)

        for c in self.cat_list:
            c.walls = self.wall_list
            c.cats = self.cat_list

    def update(self):
        self.cat_list.update()
        self.player.update()
        self.wind_list.update()


# End Screen
class EndScreen(Round):
    """ The end screen for this game. """

    def __init__(self, player):
        Round.__init__(self, player)

        self.round_number = 6

        self.num_of_cats = 32

        self.entrance_coordinates = [0 * 32, 11 * 32]
        self.player.rect.x = self.entrance_coordinates[0]
        self.player.rect.y = self.entrance_coordinates[1]
        self.exit_coordinates = [-100, -100]

        self.background = pygame.image.load(constants.BACKGROUND_END_SCREEN).convert()

        self.music = pygame.mixer.Sound(constants.MUSIC_END)
        self.music.set_volume(constants.DEFAULT_SOUND_LEVEL)

        self.cat_list = pygame.sprite.Group()
        for y in range(160, 20 * self.num_of_cats, 20):
            self.cat_list.add(NyanCat(-52, y))

    def update(self):
        self.player.update()
        self.wind_list.update()
        self.cat_list.update()

        if self.player.rect.x >= constants.SCREEN_WIDTH or self.player.rect.x < 0:
            self.player.rect.x = self.entrance_coordinates[0]
            self.player.rect.y = self.entrance_coordinates[1]
        if self.player.rect.y >= constants.SCREEN_HEIGHT or self.player.rect.y < 0:
            self.player.rect.x = self.entrance_coordinates[0]
            self.player.rect.y = self.entrance_coordinates[1]

        for w in self.wind_list:
            if (w.rect.x >= constants.SCREEN_WIDTH or w.rect.x < 0) or \
                    (w.rect.y >= constants.SCREEN_HEIGHT or w.rect.y < 0):
                self.wind_list.remove(w)
