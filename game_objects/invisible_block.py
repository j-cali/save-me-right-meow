"""
    This module is used to define an invisible block.
"""
import pygame
import constants as constants

class InvisibleBlock(pygame.sprite.Sprite):
    """ An invisible block object (32x32) used for collision detection.

    Attributes:
        image (Surface): the image for this sprite.
        rect (rect): the rectangular coordinates for this sprite.
        rect.x (int): x coordinate of this sprite.
        rect.y (int): y coordinate of this sprite.
        player_allowed (bool): if true the player can go over this sprite, otherwise they cannot.
    """

    def __init__(self, x, y):
        """ Initialize InvisibleBlock.

        Arguments:
          x (int): x coordinate of this sprite.
          y (int): y coordinate of this sprite.
        """

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(constants.INVISIBLE_BLOCK_IMG)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # used for player spawn spot (enemies can't go in player spawn, but player can)
        self.player_allowed = False

    def set_player_allowed(self, condition):
        """ Set this block to be player allowed or not player allowed.

        Arguments:
            condition: True or False
        Returns:
            None: Sets the player_allowed to the condition argument.
        """
        self.player_allowed = condition

    def is_player_allowed(self):
        """ Returns if player is allowed.

        Returns:
            bool: True if the player is allowed, False if not.
        """
        return self.player_allowed
