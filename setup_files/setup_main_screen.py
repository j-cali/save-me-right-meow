"""  This module is for setting up the main screen """
import random

import pygame

import constants as constants
from characters.cat import Cat
from game_objects.invisible_block import InvisibleBlock


def add_invisible_blocks(list_wall):
    """ Adds the appropriate invisible blocks on the screen. Used for collision detection.

    Arguments:
        list_wall: list of walls in the game.
    Returns:
        None
    """

    # for tent
    list_wall.add(InvisibleBlock(4 * 32, 9 * 32))
    for x in range(3 * 32, (5 + 1) * 32, 32):
        for y in range(10 * 32, (11 + 1) * 32, 32):
            if x == 4 * 32 and y == 11 * 32:
                continue
            list_wall.add(InvisibleBlock(x, y))


def add_outer_walls(list_wall):
    """ Adds the appropriate walls for the screen. Used for collision detection.

    Arguments:
        list_wall: list of walls in the game.
    Returns:
        None
    """

    # for upper part of screen
    for x in range(0 * 32, (31 + 1) * 32, 32):
        for y in range(0 * 32, (3 + 1) * 32, 32):
            list_wall.add(InvisibleBlock(x, y))

    # for lower part of screen
    for x in range(0 * 32, (31 + 1) * 32, 32):
        for y in range(17 * 32, (19 + 1) * 32, 32):
            list_wall.add(InvisibleBlock(x, y))

    # for sides
    for y in range(3 * 32, (16 + 1) * 32, 32):
        if y == 11 * 32:
            list_wall.add(InvisibleBlock(0, y))
            continue
        else:
            list_wall.add(InvisibleBlock(0, y))
            list_wall.add(InvisibleBlock(constants.SCREEN_WIDTH - 32, y))


def add_inner_walls(list_wall):
    """ Adds the appropriate walls for the screen. Used for collision detection.

    Arguments:
        list_wall: list of walls in the game.
    Returns:
        None
    """

    # for first row
    for x in range(6 * 32, (22 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(x, 7 * 32))

    # for middle three horizontal rows
    for x in range(8 * 32, (20 + 1) * 32, 32):
        for y in range(9 * 32, (13 + 1) * 32, 64):
            list_wall.add(InvisibleBlock(x, y))

    # for last row
    for x in range(3 * 32, (23 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(x, 15 * 32))

    # for two rows near exit
    for x in range(22 * 32, (30 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(x, 9 * 32))
        list_wall.add(InvisibleBlock(x, 13 * 32))

    # for single blocks
    list_wall.add(InvisibleBlock(22 * 32, 8 * 32), InvisibleBlock(22 * 32, 14 * 32))
    list_wall.add(InvisibleBlock(30 * 32, 10 * 32), InvisibleBlock(30 * 32, 12 * 32))

    # for two vertical walls
    for y in range(8 * 32, (11 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(6 * 32, y))

    for y in range(12 * 32, (14 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(3 * 32, y))


def generate_cats(list_wall, num_cats, player_obj):
    """ Generates the cats for this round. Makes sure the cats don't overlap with other sprites.

    Arguments:
        list_wall: list of walls in the game.
        num_cats: the number of cats desired.
        player_obj: the player or main character.
    Returns:
        pygame.sprite.Group(): a group of cat sprites.
    """

    cat_list = pygame.sprite.Group()
    first_half = num_cats // 2
    second_half = num_cats - first_half

    for e in range(0, first_half):
        rand_x = random.randint(1, 30) * 32
        rand_y = random.randint(4, 6) * 32
        curr_cat = Cat(rand_x, rand_y)
        while ( (pygame.sprite.spritecollideany(curr_cat, list_wall) is not None) or \
                (pygame.sprite.spritecollideany(curr_cat, cat_list) is not None) or \
                (pygame.sprite.collide_rect(curr_cat, player_obj)) ):
            curr_cat = Cat(random.randint(1, 30) * 32, random.randint(4, 6) * 32)
        cat_list.add(curr_cat)

    for e in range(0, second_half):
        rand_x = random.randint(1, 30) * 32
        curr_cat = Cat(rand_x, 16 * 32)
        while (pygame.sprite.spritecollideany(curr_cat, list_wall) is not None) or \
                (pygame.sprite.spritecollideany(curr_cat, cat_list) is not None) or \
                (pygame.sprite.collide_rect(curr_cat, player_obj)):
            curr_cat = Cat(random.randint(1, 30) * 32, 16 * 32)
        cat_list.add(curr_cat)

    return cat_list
