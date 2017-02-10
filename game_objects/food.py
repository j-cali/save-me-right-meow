"""
    This module is used to define a food item.
"""
import random
import pygame
import constants as constants
from spritesheet_functions import SpriteSheet


class Food(pygame.sprite.Sprite):
    """ A food item an enemy or cat can eat.

    Attributes:
        image (Surface): the image for this sprite.
        rect (rect): the rectangular coordinates for this sprite.
        rect.x (int): x coordinate of this sprite.
        rect.y (int): y coordinate of this sprite.
    """

    def __init__(self, x, y):
        """ Initialize Food.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        pygame.sprite.Sprite.__init__(self)

        # get the sprite sheet
        self.sprite_sheet = SpriteSheet(constants.FOOD_IMG)

        self.image = self.get_food_image(random.randint(1, 5)) # get a random food item
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_food_image(self, food_number):
        """ Get the food image according to food_number.

        Arguments:
            food_number: an integer that represents a food item.
        Returns:
            Surface: an image of the food item.
        """
        if food_number == 1:
            return self.sprite_sheet.get_image(73, 113, 24, 12)  # chicken leg
        elif food_number == 2:
            return self.sprite_sheet.get_image(451, 59, 16, 16)  # french fries
        elif food_number == 3:
            return self.sprite_sheet.get_image(274, 212, 30, 18)  # pizza
        elif food_number == 4:
            return self.sprite_sheet.get_image(415, 7, 20, 20)  # burger
        else:
            return self.sprite_sheet.get_image(7, 213, 19, 15)  # taco
