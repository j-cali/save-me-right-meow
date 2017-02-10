"""
    This module is used to define a destroyable object (aka obstacles).
"""
import pygame
import constants as constants


class DestroyableObject(pygame.sprite.Sprite):
    """ A destroyable object the player can destroy with its wind power.

    Attributes:
        image (Surface): the image for this sprite.
        rect (rect): the rectangular coordinates for this sprite.
        rect.x (int): x coordinate of this sprite.
        rect.y (int): y coordinate of this sprite.
    """

    def __init__(self, x, y):
        """ Initialize DestroyableObject.

        Arguments:
            x (int): x coordinate of this sprite.
            y (int): y coordinate of this sprite.
        """

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(constants.DESTROYABLE_OBJECT_IMG)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
