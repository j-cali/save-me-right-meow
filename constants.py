"""
    Global constants used for 'Save Me Right Meow'
"""

"""
    GAME INFO
"""
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 30
GAME_TIME = 240

# For characters
POSSIBLE_DIRECTIONS = ["N", "S", "E", "W"]

# Player information
MAX_WIND_SPEED = 10
WALK_SPEED = 8
PLAYER_LIVES = 9
PLAYER_WIND_AMMO = 1
PLAYER_WIND_SPEED = 1
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

# Score values for enemies
LION_VALUE = 2
WOLF_VALUE = 4
RACCOON_VALUE = 6
LIZARD_VALUE = 8
DRAGON_VALUE = 10
CAT_VALUE = 20
BOSS_VALUE = 50

# Lives for each enemy
LION_LIVES = 1
WOLF_LIVES = 1
RACCOON_LIVES = 1
LIZARD_LIVES = 1
DRAGON_LIVES = 3
BOSS_LIVES = 20

# Game Object Images
DESTROYABLE_OBJECT_IMG = "game_resources/images/rock.png"
FOOD_IMG = "game_resources/images/food_items.png"
INVISIBLE_BLOCK_IMG = "game_resources/images/transparent_block.png"
WIND_IMG = "game_resources/images/wind.png"

# Characters Images
MAIN_CHARACTER_IMG = "game_resources/images/main_character.png"
CAT_IMG = "game_resources/images/spotted_cat.png"
NYAN_CAT_IMG = "game_resources/images/nyan_cat.png"
LION_IMG = "game_resources/images/red_lion.png"
WOLF_IMG = "game_resources/images/wolf.png"
RACCOON_IMG = "game_resources/images/raccoon.png"
LIZARD_IMG = "game_resources/images/lizard.png"
DRAGON_IMG = "game_resources/images/dragon.png"
BOSS_IMG = "game_resources/images/boss.png"

"""
    COLOR
"""
BLACK = (0, 0, 0)
BLOOD_RED = (138, 7, 7)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 128, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

"""
    FONT
"""
FONT1 = "game_resources/fonts/digital-7/digital-7.ttf"
FONT2 = "game_resources/fonts/green-fuz/green_fuz.otf"
FONT3 = "game_resources/fonts/kaushan-script/KaushanScript-Regular.otf"

"""
    MUSIC
"""
MUSIC_MAIN = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
MUSIC_END = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
MUSIC_ROUND1 = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
MUSIC_ROUND2 = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
MUSIC_ROUND3 = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
MUSIC_ROUND4 = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
MUSIC_ROUND5 = "game_resources/sounds/lotagblanco_-_slumlord.ogg"
SOUND_WIND = "game_resources/sounds/wind_sound.ogg"
DEFAULT_SOUND_LEVEL = 0.3

"""
    BACKGROUND
"""
BACKGROUND_ROUND1 = "game_resources/images/background_round1.png"
BACKGROUND_ROUND2 = "game_resources/images/background_round2.png"
BACKGROUND_ROUND3 = "game_resources/images/background_round3.png"
BACKGROUND_ROUND4 = "game_resources/images/background_round4.png"
BACKGROUND_ROUND5 = "game_resources/images/background_round5.png"
BACKGROUND_MAIN_SCREEN = "game_resources/images/main_screen.png"
BACKGROUND_END_SCREEN = "game_resources/images/end_screen.png"
HELP_BACKGROUND = "game_resources/images/instruction_screen.png"


"""
    TEXT
"""
STORY_1 = "Story:"
STORY_2 = "One day you wake up to find yourself in another dimension . . . or a dream?"
STORY_3 = "You don't know where you are and why you are here . . . wait . . ."
STORY_4 = "You see many creatures from lions to lizard men . . ."
STORY_5 = "AGH! CATS! (btw you are allergic to cats)"
STORY_6 = "Plot twist: You must save the cats to easily progress this universe (game)."

OBJECTIVE_1 = "Objective:"
OBJECTIVE_2 = "Shoot enemies (moving enemies that are not cats) with your wind power."
OBJECTIVE_3 = "Cats can't be destroyed with your wind power."
OBJECTIVE_4 = "Drop food to save the cats. Feeding the cats will also increase your wind ammo."
OBJECTIVE_5 = "Enemies can eat the food you drop and increase their speed, so be careful."
OBJECTIVE_6 = "Cats and enemies can take your life, you start with 9 lives (like a cat)."
OBJECTIVE_7 = "When you die, your wind ammo and wind speed reset to 1."
OBJECTIVE_8 = "Each round you pass you gain one extra life and +30 seconds to your time."
OBJECTIVE_9 = "Get points by destroying enemies and saving cats. Pass all rounds to win the game."

INSTRUCTION_1 = "Use the arrow keys to move up, down, left, or right."
INSTRUCTION_2 = "Use the space bar button to create winds and destroy things."
INSTRUCTION_3 = "Destroy rocks to increase your wind speed."
INSTRUCTION_4 = "Destroy enemies to increase your food inventory."
INSTRUCTION_5 = "Help save the cats by dropping food (pressing down the x button)."
INSTRUCTION_5_1 = "Caution: If an enemy eats these instead, the enemy will increase its speed."
INSTRUCTION_6 = "Rack up food inventory to save cats, and in turn gaining more wind ammo."
INSTRUCTION_7 = "Have a purrrrfect rescue!!"
