""" This module is used to define the Main Character of the game 'Save Me Right Meow', aka the player. """
import pygame
import constants as constants
import setup_files.setup_images as set_img
from characters.cat import Cat
from characters.enemy import Enemy
from game_objects.invisible_block import InvisibleBlock
from game_objects.wind import Wind
from spritesheet_functions import SpriteSheet


class MainCharacter(pygame.sprite.Sprite):
    """ The enemy character for the player to avoid...or destroy.

    Attributes:
        MAX_WIND_SPEED (int): the max speed for the player's winds.
        WALK_SPEED (int): the walk speed of the player.
        change_x (int): the current change in x for the player.
        change_y (int): the current change in y for the player.
        walking_frames_l (list): list of left facing images.
        walking_frames_r (list): list of right facing images.
        walking_frames_u (list): list of up facing images.
        walking_frames_d (list): list of down facing images.
        direction (str): the direction this sprite is facing.
        sprite_sheet (SpriteSheet): the sprite sheet for this sprite.
        current_round (Round): the current round the player is in.
        alive (bool): True if the player is alive, False otherwise.
        score (int): the player's current score.
        lives (int): the player's current number of lives.
        food_inventory (int): the number of food items the player has.
        wind_ammo (int): how much winds the player can produce.
        wind_speed (int): how fast the player's winds are.
    """

    # max wind speed a player can create
    MAX_WIND_SPEED = constants.MAX_WIND_SPEED

    # how fast the player walks
    WALK_SPEED = constants.WALK_SPEED

    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left, right, up, downs for the player
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []

    # the direction the player is facing
    direction = "E"

    def __init__(self):
        """ Initialize MainCharacter. """

        pygame.sprite.Sprite.__init__(self)

        # get the sprite sheet
        self.sprite_sheet = SpriteSheet(constants.MAIN_CHARACTER_IMG)

        self.current_round = None
        self.alive = True
        self.score = 0
        self.lives = constants.PLAYER_LIVES
        self.food_inventory = 0
        self.wind_ammo = constants.PLAYER_WIND_AMMO
        self.wind_speed = constants.PLAYER_WIND_SPEED

        # set the images
        set_img.set_player_img(self.sprite_sheet, self.walking_frames_d, self.walking_frames_r,
                               self.walking_frames_l, self.walking_frames_u)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect and initialize starting position
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, screen):
        """ Draw the player onto the screen.

        Arguments:
            screen: the screen the player is going to be drawn into.
        Returns:
            None
        """

        screen.blit(self.image, [self.rect.x, self.rect.y])

    def update(self):
        """ Update MainCharacter accordingly.

        Returns:
            None
        """

        current_lives = self.lives

        if self.lives == 0:
            self.alive = False
            print("GAME OVER.")
        else:

            # move left/right
            self.rect.x += self.change_x
            pos_x = self.rect.x

            # check for collisions
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if (issubclass(type(obj), Enemy) or type(obj) is Cat) and self.current_round.round_number != 0:
                    self.lives -= 1

                if type(obj) is InvisibleBlock:
                    if obj.is_player_allowed():
                        continue

                if type(obj) is Wind:
                    continue

                if self.change_x > 0:
                    self.rect.right = obj.rect.left
                else:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = obj.rect.right

            # move up/down
            self.rect.y += self.change_y
            pos_y = self.rect.y

            # Check and see if we hit anything
            all_collisions = self.get_collisions()
            for obj in all_collisions:
                if (issubclass(type(obj), Enemy) or type(obj) is Cat) and self.current_round.round_number != 0:
                    self.lives -= 1

                if type(obj) is InvisibleBlock:
                    if obj.is_player_allowed():
                        continue

                if type(obj) is Wind:
                    continue

                if self.change_y > 0:
                    self.rect.bottom = obj.rect.top
                else:
                    self.rect.top = obj.rect.bottom

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

            if self.lives != current_lives:
                self.rect.x = self.current_round.entrance_coordinates[0]
                self.rect.y = self.current_round.entrance_coordinates[1]
                self.wind_speed = 1
                self.wind_ammo = 1

    def go_left(self):
        """ Move the player left.

        Returns:
            None
        """
        self.change_x = -self.WALK_SPEED
        self.direction = "W"

    def go_right(self):
        """ Move the player right.

        Returns:
            None
        """
        self.change_x = self.WALK_SPEED
        self.direction = "E"

    def go_up(self):
        """ Move the player up.

        Returns:
            None
        """
        self.change_y = -self.WALK_SPEED
        self.direction = "N"

    def go_down(self):
        """ Move the player down.

        Returns:
            None
        """
        self.change_y = self.WALK_SPEED
        self.direction = "S"

    def stop(self):
        """ Stop the player.

        Returns:
            None
        """
        self.change_x = 0
        self.change_y = 0

    def get_collisions(self):
        """ Get the collisions (if any) from this sprite and all the other sprites in the current round.

        Returns:
            pygame.sprite.Group(): a list of the collisions between this sprite and the other sprites in this round.
        """

        all_collisions = pygame.sprite.Group()
        all_collisions.add(pygame.sprite.spritecollide(self, self.current_round.wall_list, False),
                           pygame.sprite.spritecollide(self, self.current_round.obstacle_list, False),
                           pygame.sprite.spritecollide(self, self.current_round.enemy_list, False),
                           pygame.sprite.spritecollide(self, self.current_round.cat_list, False))
        return all_collisions

    def decrease_food(self):
        """ Decrease the player's food inventory by 1.

        Returns:
            None
        """
        self.food_inventory -= 1

    def increase_food(self):
        """ Increase the player's food inventory by 1.

        Returns:
            None
        """
        self.food_inventory += 1

    def increase_max_wind(self):
        """ Increase the player's wind ammo by 1.

        Returns:
            None
        """
        self.wind_ammo += 1

    def increase_wind_speed(self):
        """ Increase the player's wind speed by 1.

        Returns:
            None
        """
        if self.wind_speed < self.MAX_WIND_SPEED:
            self.wind_speed += 1

    def increase_score(self, score):
        """ Increase the player's score by the 'score' param.

        Arguments:
            score: the score the player earned.
        Returns:
            None
        """
        self.score += score
