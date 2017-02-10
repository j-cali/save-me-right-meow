""" This module is used to define the Cat characters for 'Save Me Right Meow'. """
import random

import constants as constants
import pygame

import setup_files.setup_images as set_img
from spritesheet_functions import SpriteSheet


class Cat(pygame.sprite.Sprite):
    """ The infamous cat character. Meow!

    Attributes:
        walking_frames_l (list): list of left facing images.
        walking_frames_r (list): list of right facing images.
        walking_frames_u (list): list of up facing images.
        walking_frames_d (list): list of down facing images.
        SCORE_VALUE (int): the score value for this sprite.
        sprite_sheet (SpriteSheet): the sprite sheet for this sprite.
        image (Surface): the image for this sprite.
        rect (rect): the rectangular coordinates for this sprite.
        rect.x (int): x coordinate of this sprite.
        rect.y (int): y coordinate of this sprite.
        walls (list): the list of walls in the current round.
        obstacles (list): the list of obstacles in the current round.
        enemies (list): the list of enemies in the current round.
        cats (list): the list of cats in the current round.
        direction (str): the direction this sprite is facing.
        cat_speed (int): the speed of this cat sprite.
    """

    # This holds all the images for the animated walk left, right, up, downs for the cat
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []

    SCORE_VALUE = constants.CAT_VALUE

    def __init__(self, x, y):
        """ Initialize Cat.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        pygame.sprite.Sprite.__init__(self)

        # get the sprite sheet + set the image
        self.sprite_sheet = SpriteSheet(constants.CAT_IMG)

        # set the images
        set_img.set_cat_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                            self.walking_frames_l, self.walking_frames_u)

        # Set the image the cat starts with
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # the other sprites in this round the Cat can interact with
        self.walls = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.cats = pygame.sprite.Group()

        # random number from 1-4: (0 - North, 1 - South, 2 - East, 3 - West) NSEW
        self.direction = constants.POSSIBLE_DIRECTIONS[random.randrange(0, 4)]

        # a random speed will be given to the cat
        self.cat_speed = random.randrange(3, 7)

    def update(self):
        """ Update the Cat accordingly.

        Returns:
            None
        """
        if self.direction == "N":
            self.rect.y -= self.cat_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.top = obj.rect.bottom
                self.change_direction(1)

        if self.direction == "S":
            self.rect.y += self.cat_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.bottom = obj.rect.top
                self.change_direction(2)

        if self.direction == "E":
            self.rect.x += self.cat_speed
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if self is obj:
                    continue
                self.rect.right = obj.rect.left
                self.change_direction(3)

        if self.direction == "W":
            self.rect.x -= self.cat_speed
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


class NyanCat(Cat):
    """ A subclass of the Cat character. This NyanCat is used for the victory screen. Nyaaaa!!!

    Attributes:
        img_index (int): the current index in the list of images.
    """

    def __init__(self, x, y):
        """ Initialize NyanCat.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        Cat.__init__(self, x, y)

        # get the sprite sheet
        self.sprite_sheet = SpriteSheet(constants.NYAN_CAT_IMG)
        self.images = []

        # images
        image = self.sprite_sheet.get_image(2, 4, 52, 20)
        self.images.append(image)
        image = self.sprite_sheet.get_image(63, 4, 52, 20)
        self.images.append(image)
        image = self.sprite_sheet.get_image(123, 4, 52, 20)
        self.images.append(image)
        image = self.sprite_sheet.get_image(186, 4, 52, 20)
        self.images.append(image)
        image = self.sprite_sheet.get_image(244, 4, 52, 20)
        self.images.append(image)

        # Set the image the cat starts with
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.img_index = 0

    def update(self):
        """ Update NyanCat accordingly.

        Returns:
            None
        """

        self.rect.x += 8

        # if nyan cat goes out of bounds reset its position
        if self.rect.x >= constants.SCREEN_WIDTH:
            self.rect.x = 0

        self.img_index += 1

        if self.img_index >= len(self.images):
            self.img_index = 0

        self.image = self.images[self.img_index]
