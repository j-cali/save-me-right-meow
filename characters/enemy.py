""" This module is used to define the enemies in this game. """
import random
import pygame
import constants as constants
import setup_files.setup_images as set_img
from spritesheet_functions import SpriteSheet


class Enemy(pygame.sprite.Sprite):
    """ The enemy character for the player to avoid...or destroy.

    Attributes:
        image (Surface): the image for this sprite.
        sprite_sheet (SpriteSheet): the sprite sheet for this sprite.
        enemy_speed (int): the speed of this enemy sprite.
        SCORE_VALUE (int): the score value for this sprite.
        lives (int): the number of lives this enemy has.
        walking_frames_l (list): list of left facing images.
        walking_frames_r (list): list of right facing images.
        walking_frames_u (list): list of up facing images.
        walking_frames_d (list): list of down facing images.
        walls (list): the list of walls in the current round.
        obstacles (list): the list of obstacles in the current round.
        enemies (list): the list of enemies in the current round.
        cats (list): the list of cats in the current round.
        direction (str): the direction this sprite is facing.
    """

    image = None
    sprite_sheet = None
    enemy_speed = None
    SCORE_VALUE = None
    lives = 1  # the default number of lives an enemy has is 1

    def __init__(self, x, y):
        """ Initialize Enemy.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        pygame.sprite.Sprite.__init__(self)

        # This holds all the images for the animated walk left, right, up, downs for the enemy
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []

        # the other sprites in this round the Enemy can interact with
        self.walls = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.cats = pygame.sprite.Group()

        # random number from 1-4: (0 - North, 1 - South, 2 - East, 3 - West) NSEW
        self.direction = constants.POSSIBLE_DIRECTIONS[random.randrange(0, 4)]

    def update(self):
        """ Update the Enemy accordingly.

        Returns:
            None
        """
        if self.direction == "N":
            self.rect.y -= self.enemy_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.top = obj.rect.bottom
                self.change_direction(1)

        if self.direction == "S":
            self.rect.y += self.enemy_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.bottom = obj.rect.top
                self.change_direction(2)

        if self.direction == "E":
            self.rect.x += self.enemy_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.right = obj.rect.left
                self.change_direction(3)

        if self.direction == "W":
            self.rect.x -= self.enemy_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.left = obj.rect.right
                self.change_direction(4)

        self.update_frame(self.rect.x, self.rect.y)

    def get_collisions(self):
        """ Get the collisions (if any) from this sprite and all the other sprites in the current round.

        Returns:
            pygame.sprite.Group(): a list of the collisions between this sprite and the other sprites in this round.
        """

        all_collisions = pygame.sprite.Group()
        all_collisions.add(pygame.sprite.spritecollide(self, self.walls, False),
                           pygame.sprite.spritecollide(self, self.obstacles, False),
                           pygame.sprite.spritecollide(self, self.enemies, False),
                           pygame.sprite.spritecollide(self, self.cats, False))
        return all_collisions

    def change_direction(self, current_direction):
        """ Change the direction of this sprite.

        Arguments:
            current_direction: the current direction this sprite is facing.
        Returns:
            None
        """

        new_direction = current_direction
        while new_direction == current_direction:
            new_direction = constants.POSSIBLE_DIRECTIONS[random.randrange(0, 4)]
        self.direction = new_direction

    def update_frame(self, pos_x, pos_y):
        """ Update the current image of this sprite.

        Arguments:
            pos_x: the x coordinate of this sprite.
            pos_y: the y coordinate of this sprite.
        Returns:
            None
        """

        if self.direction == "E":
            frame = (pos_x // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        if self.direction == "W":
            frame = (pos_x // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if self.direction == "N":
            frame = (pos_y // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        if self.direction == "S":
            frame = (pos_y // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]

    def increase_speed(self):
        """ Increases the enemy speed by 1.

        Returns:
            None
        """
        self.enemy_speed += 1

    def decrease_lives(self):
        """ Decreases the enemy's lives by 1.

        Returns:
            None
        """
        if self.lives == 0:
            self.lives = 0
        else:
            self.lives -= 1

""" END OF SUPER CLASS """


"""
    BELOW ARE THE POSSIBLE ENEMIES THAT ARE SUBCLASSES OF THE ENEMY CLASS.
    I only document the first class (Lion) since the rest of the enemies are of the same form as Lion.
"""


class Lion(Enemy):
    """ Definition for the Enemy: Lion. """

    # score value for Lion
    SCORE_VALUE = constants.LION_VALUE

    def __init__(self, x, y):
        """ Initialize Lion.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Enemy.__init__(self, x, y)

        # get the sprite sheet
        self.sprite_sheet = SpriteSheet(constants.LION_IMG)

        # set the images
        set_img.set_lion_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                             self.walking_frames_l, self.walking_frames_u)

        # set the initial image to be the enemy facing right
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # this Lion's speed
        self.enemy_speed = random.randrange(2, 4)

        # the amount of lives this Lion has
        self.lives = constants.LION_LIVES


class Wolf(Enemy):
    """ Definition for the Enemy: Wolf. """

    SCORE_VALUE = constants.WOLF_VALUE

    def __init__(self, x, y):
        """ Initialize Wolf.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Enemy.__init__(self, x, y)

        self.sprite_sheet = SpriteSheet(constants.WOLF_IMG)

        set_img.set_wolf_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                             self.walking_frames_l, self.walking_frames_u)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.enemy_speed = random.randrange(3, 5)
        self.lives = constants.WOLF_LIVES


class Raccoon(Enemy):
    """ Definition for the Enemy: Raccoon. """

    SCORE_VALUE = constants.RACCOON_VALUE

    def __init__(self, x, y):
        """ Initialize Raccoon.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Enemy.__init__(self, x, y)

        self.sprite_sheet = SpriteSheet(constants.RACCOON_IMG)

        set_img.set_raccoon_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                                self.walking_frames_l, self.walking_frames_u)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.enemy_speed = random.randrange(4, 6)
        self.lives = constants.RACCOON_LIVES


class Lizard(Enemy):
    """ Definition for the Enemy: Lizard. """

    SCORE_VALUE = constants.LIZARD_VALUE

    def __init__(self, x, y):
        """ Initialize Lizard.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Enemy.__init__(self, x, y)

        self.sprite_sheet = SpriteSheet(constants.LIZARD_IMG)

        set_img.set_lizard_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                               self.walking_frames_l, self.walking_frames_u)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.enemy_speed = random.randrange(5, 7)
        self.lives = constants.LIZARD_LIVES


class Dragon(Enemy):
    """ Definition for the Enemy: Dragon. """

    SCORE_VALUE = constants.DRAGON_VALUE

    def __init__(self, x, y):
        """ Initialize Dragon.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Enemy.__init__(self, x, y)

        self.sprite_sheet = SpriteSheet(constants.DRAGON_IMG)

        set_img.set_dragon_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                               self.walking_frames_l, self.walking_frames_u)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.enemy_speed = random.randrange(8, 10)
        self.lives = constants.DRAGON_LIVES


class Boss(Enemy):
    """ Definition for the Enemy: Boss. """

    SCORE_VALUE = constants.BOSS_VALUE

    def __init__(self, x, y):
        """ Initialize Boss.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Enemy.__init__(self, x, y)

        self.sprite_sheet = SpriteSheet(constants.BOSS_IMG)

        set_img.set_boss_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                             self.walking_frames_l, self.walking_frames_u)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.enemy_speed = 4
        self.lives = constants.BOSS_LIVES
