"""  This module is for setting up round 3. """
import random
import pygame
import constants as constants
from characters.cat import Cat
from characters.enemy import Raccoon
from game_objects.invisible_block import InvisibleBlock
from game_objects.destroyable_object import DestroyableObject


def add_invisible_blocks(list_wall, spawn_coordinates):
    """ Adds the appropriate invisible blocks on the screen. Used for collision detection.

    Arguments:
        list_wall: list of walls in the game.
        spawn_coordinates: the spawn coordinates for when a player dies.
    Returns:
        None
    """

    # player spawn
    player_spawn = InvisibleBlock(spawn_coordinates[0], spawn_coordinates[1])
    player_spawn.set_player_allowed(True)
    list_wall.add(player_spawn)

    # for tombstones (3)
    list_wall.add(InvisibleBlock(4 * 32, 2 * 32), InvisibleBlock(4 * 32, 3 * 32), InvisibleBlock(4 * 32, 4 * 32))

    # for dragon statues
    for x in range(1 * 32, (4 + 1) * 32, 32):
        for y in range(13 * 32, (14 + 1) * 32, 32):
            list_wall.add(InvisibleBlock(x, y))

    # for bridge area
    for x in range(4 * 32, (11 + 1) * 32, 32):
        for y in range(9 * 32, (11 + 1) * 32, 32):
            if y == 10 * 32:
                continue
            list_wall.add(InvisibleBlock(x, y))

    # for exit area
    for x in range(1 * 32, (3 + 1) * 32, 32):
        for y in range(2 * 32, (6 + 1) * 32, 32):
            if x == 2 * 32:
                if y == 4 * 32 or y == 5 * 32 or y == 6 * 32:
                    continue
            list_wall.add(InvisibleBlock(x, y))


def add_outer_walls(list_wall):
    """ Adds the appropriate walls for the screen. Used for collision detection.

    Arguments:
        list_wall: list of walls in the game.
    Returns:
        None
    """

    # Create upper and lower borders
    horizontal_start_x = 32
    hor_upper_end_x = 32 * (30 + 1)
    hor_lower_end_x = 32 * (30 + 1)
    lower_border_y = constants.SCREEN_HEIGHT - 32
    upper_border_y = 32

    for hor_x in range(horizontal_start_x, hor_upper_end_x, 32):
        list_wall.add(InvisibleBlock(hor_x, upper_border_y))

    for hor_x in range(horizontal_start_x, hor_lower_end_x, 32):
        list_wall.add(InvisibleBlock(hor_x, lower_border_y))

    # Create left and right borders
    vertical_start_y = 32
    vertical_end_y = 32 * (19 + 1)  # 19 blocks down
    left_border_x = 0
    right_border_x = constants.SCREEN_WIDTH - 32

    for ver_y in range(vertical_start_y, vertical_end_y, 32):
        list_wall.add(InvisibleBlock(left_border_x, ver_y))
        list_wall.add(InvisibleBlock(right_border_x, ver_y))


def add_inner_walls(list_wall):
    """ Adds the appropriate walls for the screen. Used for collision detection.

    Arguments:
        list_wall: list of walls in the game.
    Returns:
        None
    """

    # for curvy walls
    for x in range(1 * 32, (5 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(x, 15 * 32))

    list_wall.add(InvisibleBlock(5 * 32, 13 * 32), InvisibleBlock(5 * 32, 14 * 32))

    for x in range(5 * 32, (15 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(x, 12 * 32))

    for y in range(7 * 32, (11 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(15 * 32, y))

    for x in range(7 * 32, (15 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(x, 6 * 32))

    # 3 horizontal lines
    for x in range(7 * 32, (29 + 1) * 32, 64):
        list_wall.add(InvisibleBlock(x, 4 * 32))

    for x in range(7 * 32, (29 + 1) * 32, 64):
        list_wall.add(InvisibleBlock(x, 14 * 32))

    for x in range(7 * 32, (29 + 1) * 32, 64):
        list_wall.add(InvisibleBlock(x, 16 * 32))

    # for square-like grid in center (walls)
    for x in range(17 * 32,(29 + 1) * 32, 64):
        for y in range(6 * 32,(12 + 1) * 32, 64):
            list_wall.add(InvisibleBlock(x, y))

    # walls near exit
    for y in range(5 * 32, (8 + 1) * 32, 32):
        list_wall.add(InvisibleBlock(4 * 32, y))


def generate_obstacles(list_wall, num_obstacles, player_obj):
    """ Generates the obstacles for this round. Makes sure the obstacles don't overlap with other sprites.

    Arguments:
        list_wall: list of walls in the game.
        num_obstacles: the number of obstacles desired.
        player_obj: the player or main character.
    Returns:
        pygame.sprite.Group(): a group of obstacle sprites.
    """

    obstacle_list = pygame.sprite.Group()

    obstacle_list.add(DestroyableObject(1 * 32, 17 * 32), DestroyableObject(2 * 32, 18 * 32))

    for x in range(0, num_obstacles):
        rand_x = random.randint(1, 30) * 32
        rand_y = random.randint(2, 18) * 32
        obs = DestroyableObject(rand_x, rand_y)
        while (pygame.sprite.spritecollideany(obs, list_wall) is not None) or \
                (pygame.sprite.spritecollideany(obs, obstacle_list) is not None) or \
                (pygame.sprite.collide_rect(obs, player_obj)):
            obs = DestroyableObject(random.randint(1, 30) * 32, random.randint(2, 18) * 32)
        obstacle_list.add(obs)

    return obstacle_list


def generate_enemies(list_wall, num_enemies, player_obj):
    """ Generates the enemies for this round. Makes sure the enemies don't overlap with other sprites.

    Arguments:
        list_wall: list of walls in the game.
        num_enemies: the number of enemies desired.
        player_obj: the player or main character.
    Returns:
        pygame.sprite.Group(): a group of enemy sprites.
    """

    enemy_list = pygame.sprite.Group()

    for e in range(0, num_enemies):
        rand_x = random.randint(1, 30) * 32
        rand_y = random.randint(2, 18) * 32
        curr_enemy = Raccoon(rand_x, rand_y)
        while (pygame.sprite.spritecollideany(curr_enemy, list_wall) is not None) or \
                (pygame.sprite.spritecollideany(curr_enemy, enemy_list) is not None) or \
                (pygame.sprite.collide_rect(curr_enemy, player_obj)):
            curr_enemy = Raccoon(random.randint(1, 30) * 32, random.randint(2, 18) * 32)
        enemy_list.add(curr_enemy)

    return enemy_list


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

    for e in range(0, num_cats):
        rand_x = random.randint(5, 30) * 32
        rand_y = random.randint(10, 18) * 32
        curr_cat = Cat(rand_x, rand_y)
        while (pygame.sprite.spritecollideany(curr_cat, list_wall) is not None) or \
                (pygame.sprite.spritecollideany(curr_cat, cat_list) is not None) or \
                (pygame.sprite.collide_rect(curr_cat, player_obj)):
            curr_cat = Cat(random.randint(5, 30) * 32, random.randint(2, 18) * 32)
        cat_list.add(curr_cat)

    return cat_list
