"""
    This module is used to define a wind.
"""
import pygame
import constants as constants
from spritesheet_functions import SpriteSheet


class Wind(pygame.sprite.Sprite):
    """ A wind sprite that can eliminate enemies and obstacle sprites.

    Attributes:
        sprite_sheet (SpriteSheet): the sprite sheet for this sprite.
        images (list): a list of all images for this sprite
        img_index (int): the current index in the list of images.
        direction (str): the direction the wind is going to head into.
        wind_speed (int): the speed of the wind.
        image (Surface): the current image for this sprite.
        rect (rect): the rectangular coordinates for this sprite.
        rect.x (int): x coordinate of this sprite.
        rect.y (int): y coordinate of this sprite.
    """

    def __init__(self, x, y, player_direction, wind_speed):
        """ Initialize Wind.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
            player_direction (str): the current direction of the player.
            wind_speed (int): the wind speed for this wind.
        """

        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = SpriteSheet(constants.WIND_IMG)
        self.images = []
        self.images.append(self.sprite_sheet.get_image(0, 0, 32, 32))
        self.images.append(self.sprite_sheet.get_image(35, 0, 32, 32))
        self.images.append(self.sprite_sheet.get_image(69, 0, 32, 32))
        self.images.append(self.sprite_sheet.get_image(103, 0, 32, 32))
        self.images.append(self.sprite_sheet.get_image(135, 0, 32, 32))
        self.img_index = 0

        self.direction = player_direction
        self.wind_speed = wind_speed

        self.image = self.images[self.img_index]
        self.rect = self.image.get_rect()

        if self.direction == "N":
            self.rect.x = x
            self.rect.y = y - 32
        elif self.direction == "S":
            self.rect.x = x
            self.rect.y = y + 32
        elif self.direction == "E":
            self.rect.x = x + 32
            self.rect.y = y
        elif self.direction == "W":
            self.rect.x = x - 32
            self.rect.y = y

    def update(self):
        """ Update the wind accordingly.

        Returns:
            None
        """
        self.img_index += 1
        if self.img_index >= len(self.images):
            self.img_index = 0
        self.image = self.images[self.img_index]

        if self.direction == "N":
            self.rect.y -= self.wind_speed
        if self.direction == "S":
            self.rect.y += self.wind_speed
        if self.direction == "W":
            self.rect.x -= self.wind_speed
        if self.direction == "E":
            self.rect.x += self.wind_speed
