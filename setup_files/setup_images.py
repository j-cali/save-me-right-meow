""" This module is used to setup the images for some characters. """
import constants as constants


def set_lion_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Lion character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    img = sheet.get_image(0, 0, 26, 32)
    down_images.append(img)
    img = sheet.get_image(34, 0, 26, 32)
    down_images.append(img)
    img = sheet.get_image(61, 0, 26, 32)
    down_images.append(img)

    # right facing images
    img = sheet.get_image(0, 65, 32, 31)
    right_images.append(img)
    img = sheet.get_image(31, 65, 32, 32)
    right_images.append(img)
    img = sheet.get_image(63, 64, 32, 32)
    right_images.append(img)

    # left facing images
    img = sheet.get_image(0, 33, 32, 32)
    left_images.append(img)
    img = sheet.get_image(32, 32, 32, 32)
    left_images.append(img)
    img = sheet.get_image(64, 31, 32, 32)
    left_images.append(img)

    # up facing images
    img = sheet.get_image(0, 95, 26, 32)
    up_images.append(img)
    img = sheet.get_image(31, 96, 26, 32)
    up_images.append(img)
    img = sheet.get_image(64, 96, 26, 32)
    up_images.append(img)


def set_wolf_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Wolf character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    img = sheet.get_image(0, 0, 25, 31)
    down_images.append(img)
    img = sheet.get_image(25, 0, 25, 31)
    down_images.append(img)
    img = sheet.get_image(50, 0, 25, 31)
    down_images.append(img)

    # right facing images
    img = sheet.get_image(0, 74, 32, 32)
    right_images.append(img)
    img = sheet.get_image(32, 74, 32, 32)
    right_images.append(img)
    img = sheet.get_image(64, 74, 32, 32)
    right_images.append(img)


    # left facing images
    img = sheet.get_image(0, 42, 32, 32)
    left_images.append(img)
    img = sheet.get_image(32, 42, 32, 32)
    left_images.append(img)
    img = sheet.get_image(65, 42, 31, 31)
    left_images.append(img)

    # up facing images
    img = sheet.get_image(0, 113, 25, 32)
    up_images.append(img)
    img = sheet.get_image(25, 112, 25, 32)
    up_images.append(img)
    img = sheet.get_image(54, 112, 26, 32)
    up_images.append(img)


def set_raccoon_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Wolf character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    img = sheet.get_image(0, 0, 32, 31)
    down_images.append(img)
    img = sheet.get_image(34, 0, 32, 32)
    down_images.append(img)
    img = sheet.get_image(65, 0, 32, 32)
    down_images.append(img)

    # right facing images
    img = sheet.get_image(0, 77, 32, 32)
    right_images.append(img)
    img = sheet.get_image(32, 77, 32, 32)
    right_images.append(img)
    img = sheet.get_image(64, 77, 31, 31)
    right_images.append(img)

    # left facing images
    img = sheet.get_image(0, 35, 32, 32)
    left_images.append(img)
    img = sheet.get_image(32, 35, 32, 32)
    left_images.append(img)
    img = sheet.get_image(64, 35, 32, 32)
    left_images.append(img)

    # up facing images
    img = sheet.get_image(0, 113, 32, 32)
    up_images.append(img)
    img = sheet.get_image(33, 113, 32, 32)
    up_images.append(img)
    img = sheet.get_image(64, 113, 32, 32)
    up_images.append(img)


def set_lizard_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Lizard character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    img = sheet.get_image(0, 0, 32, 32)
    down_images.append(img)
    img = sheet.get_image(33, 0, 32, 32)
    down_images.append(img)
    img = sheet.get_image(67, 0, 32, 32)
    down_images.append(img)

    # right facing images
    img = sheet.get_image(0, 72, 32, 32)
    right_images.append(img)
    img = sheet.get_image(32, 72, 32, 32)
    right_images.append(img)
    img = sheet.get_image(64, 72, 32, 32)
    right_images.append(img)

    # left facing images
    img = sheet.get_image(0, 36, 32, 32)
    left_images.append(img)
    img = sheet.get_image(32, 36, 32, 32)
    left_images.append(img)
    img = sheet.get_image(64, 36, 32, 32)
    left_images.append(img)

    # up facing images
    img = sheet.get_image(0, 109, 32, 32)
    up_images.append(img)
    img = sheet.get_image(32, 109, 32, 32)
    up_images.append(img)
    img = sheet.get_image(64, 109, 32, 32)
    up_images.append(img)


def set_dragon_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Dragon character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    img = sheet.get_image(0, 13, 96, 77)
    down_images.append(img)
    img = sheet.get_image(113, 11, 62, 78)
    down_images.append(img)
    img = sheet.get_image(192, 12, 97, 78)
    down_images.append(img)
    img = sheet.get_image(288, 35, 96, 56)
    down_images.append(img)

    # right facing images
    img = sheet.get_image(0, 201, 95, 71)
    right_images.append(img)
    img = sheet.get_image(97, 192, 94, 82)
    right_images.append(img)
    img = sheet.get_image(192, 196, 95, 71)
    right_images.append(img)
    img = sheet.get_image(288, 219, 96, 69)
    right_images.append(img)

    # left facing images
    img = sheet.get_image(1, 105, 95, 71)
    left_images.append(img)
    img = sheet.get_image(97, 96, 94, 82)
    left_images.append(img)
    img = sheet.get_image(193, 99, 95, 73)
    left_images.append(img)
    img = sheet.get_image(288, 122, 96, 70)
    left_images.append(img)

    # up facing images
    img = sheet.get_image(0, 292, 96, 91)
    up_images.append(img)
    img = sheet.get_image(112, 289, 64, 90)
    up_images.append(img)
    img = sheet.get_image(192, 292, 96, 91)
    up_images.append(img)
    img = sheet.get_image(288, 304, 95, 75)
    up_images.append(img)


def set_boss_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Boss character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    img = sheet.get_image(0, 5, 231, 221)
    down_images.append(img)
    img = sheet.get_image(238, 3, 213, 223)
    down_images.append(img)
    img = sheet.get_image(461, 5, 230, 221)
    down_images.append(img)
    img = sheet.get_image(703, 3, 213, 223)
    down_images.append(img)

    # right facing images
    img = sheet.get_image(0, 470, 226, 220)
    right_images.append(img)
    img = sheet.get_image(231, 465, 228, 221)
    right_images.append(img)
    img = sheet.get_image(459, 473, 227, 217)
    right_images.append(img)
    img = sheet.get_image(691, 470, 226, 217)
    right_images.append(img)

    # left facing images
    img = sheet.get_image(3, 240, 228, 218)
    left_images.append(img)
    img = sheet.get_image(232, 236, 228, 221)
    left_images.append(img)
    img = sheet.get_image(463, 240, 228, 220)
    left_images.append(img)
    img = sheet.get_image(693, 240, 227, 217)
    left_images.append(img)

    # up facing images
    img = sheet.get_image(7, 689, 220, 231)
    up_images.append(img)
    img = sheet.get_image(254, 693, 194, 224)
    up_images.append(img)
    img = sheet.get_image(466, 689, 220, 231)
    up_images.append(img)
    img = sheet.get_image(704, 693, 194, 224)
    up_images.append(img)


def set_player_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the MainCharacter.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # right facing images
    image = sheet.get_image(1, 35, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    right_images.append(image)
    image = sheet.get_image(37, 35, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    right_images.append(image)
    image = sheet.get_image(74, 34, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    right_images.append(image)

    # left facing images
    image = sheet.get_image(0, 105, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    left_images.append(image)
    image = sheet.get_image(37, 103, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    left_images.append(image)
    image = sheet.get_image(74, 103, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    left_images.append(image)

    # up facing images
    image = sheet.get_image(0, 0, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    up_images.append(image)
    image = sheet.get_image(35, 0, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    up_images.append(image)
    image = sheet.get_image(74, 0, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    up_images.append(image)

    # down facing images
    image = sheet.get_image(1, 71, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    down_images.append(image)
    image = sheet.get_image(37, 70, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    down_images.append(image)
    image = sheet.get_image(74, 70, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT)
    down_images.append(image)


def set_cat_img(sheet, down_images, right_images, left_images, up_images):
    """ Setups the image for the Cat character.

    Arguments:
        sheet: the sprite sheet for this sprite.
        down_images: the list of down facing images.
        right_images: the list of right facing images.
        left_images: the list of left facing images.
        up_images: the list of up facing images.
    Returns:
        None
    """

    # down facing images
    image = sheet.get_image(0, 0, 26, 32)
    down_images.append(image)
    image = sheet.get_image(27, 0, 26, 32)
    down_images.append(image)
    image = sheet.get_image(53, 0, 26, 32)
    down_images.append(image)

    # right facing images
    image = sheet.get_image(0, 69, 31, 32)
    right_images.append(image)
    image = sheet.get_image(31, 71, 32, 32)
    right_images.append(image)
    image = sheet.get_image(63, 72, 32, 32)
    right_images.append(image)

    # left facing images
    image = sheet.get_image(0, 34, 31, 32)
    left_images.append(image)
    image = sheet.get_image(32, 33, 32, 32)
    left_images.append(image)
    image = sheet.get_image(64, 35, 31, 29)
    left_images.append(image)

    # up facing images
    image = sheet.get_image(0, 101, 26, 32)
    up_images.append(image)
    image = sheet.get_image(27, 103, 26, 32)
    up_images.append(image)
    image = sheet.get_image(58, 104, 26, 32)
    up_images.append(image)
