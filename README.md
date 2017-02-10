TITLE: Save Me Right Meow
AUTHOR: John Calilung

HOW TO RUN / INSTALL:
    Assuming you have python and pygame installed...

    Option 1:
        1. Go to Save Me Right Meow directory where this README file is located.
        2. Then run the program from the command line:
            $ python main.py

    Option 2:
        1. Open up Save Me Right Meow folder.
        2. Double-click main.py

STORY:
    One day you wake up to find yourself in another dimension . . . or a dream?
    You don't know where you are and why you are here . . . wait . . .
    You see many creatures from lions to lizard men . . .
    AGH! CATS! (btw you are allergic to cats)
    Plot twist: You must save the cats to easily progress this universe (game).

OBJECTIVE:
    Shoot enemies (moving enemies that are not cats) with your wind power.
    Cats can't be destroyed with your wind power.
    Drop food to save the cats. Feeding the cats will also increase your wind ammo.
    Enemies can eat the food you drop and increase their speed, so be careful.
    Cats and enemies can take your life, you start with 9 lives (like a cat).
    When you die, your wind ammo and wind speed reset to 1.
    Each round you pass you gain one extra life and +30 seconds to your time.
    Get points by destroying enemies and saving cats. Get through all the rounds to win the game. Good luck!

HOW TO PLAY (INSTRUCTIONS):
    Main Controls
        - Arrow keys to move up, down, left, right
        - Space bar to shoot wind
        - 'x' to drop food
    Other
        - 'm' to turn music on/off
        - 'p' to pause the game

    Use the arrow keys to move up, down, left, or right.
    Use the space bar button to create winds and destroy things.
    Destroy rocks to increase your wind speed.
    Destroy enemies to increase your food inventory.
    Help save the cats by dropping food (pressing down the x button).
        Caution: If an enemy eats these instead, the enemy will increase its speed.
    Rack up food inventory to save cats, and in turn gaining more wind ammo.

GAME INFORMATION:
    On Rounds
        Each time you pass a round you gain one life and +30 seconds for your game time.
    On Winds
        Wind ammo does not mean how much wind remaining you can create, but how much you can produce
        before it disappears.
    On Enemies
        To destroy enemies, shoot wind at them. Enemies have a 'lives' attribute that determine their health.
        To destroy enemies with 'lives' > 1, you must hit them with winds 'lives' amount of times.
        Each round will present different enemies.
    On Scoring
        You get points for eliminating enemies and feeding/saving the cats.
        Once you finish the game, you get bonus points added to your final score.
            [Ex: Final Score = Total Score + Total cats saved + Time Remaining (in seconds) + Total lives left]
        However, you do not get these bonuses if you die in the game or run out of time.

              SCORING TABLE + CHARACTER INFORMATION
        CHARACTER         POINTS      SPEED         LIVES
        Lion                2         (2, 4)          1
        Wolf                4         (3, 5)          1
        Raccoon             6         (4, 6)          1
        Lizard              8         (5, 7)          1
        Dragon              10        (8, 10)         3
        Cat                 20        (3, 7)         n/a
        Boss                50          4             20

BUGS:
    * Dropping the food will sometimes not show the food image.
	* Round 5 - Dragon sometimes goes off screen. (Fix generate_enemies method in setup_round5.py)
	
	
	
=========================================================================
=================================SOURCES=================================
=========================================================================
Some links of the sources I used for 'Save Me Right Meow'.



========================IMAGES USED========================

dragon.png and boss.png
http://www.gdunlimited.net/forums/topic/9493-dragon-sprites/
http://www.universomaker.net/t1885-vx-ace-monstruos-ineditos

food_items.png
http://opengameart.org/content/food-items-from-crosstown-smash

lizard.png
http://forum.mfo3.pl/showthread.php?22631-Propozycje-nowych-chowa%C5%84c%C3%B3w

main_character.png
http://silveiraneto.net/2008/12/07/nerdy-guy-my-free-charset-version-2/

nyan_cat.png
http://digimonfakedrawer.deviantart.com/art/nyancat-sprite-sheet-not-completed-278201601
http://sws.smackjeeves.com/comics/1273079/a-little-bit-nyan-a-nyan-cat-sprite/

rpg_tileset.png
http://www.rpg-maker.fr/index.php?page=forum&id=21469

spotted_cat.png
http://www.rpgmakercentral.com/topic/2399-grannys-lists-animal-sprites/

red_lion.png
http://forums.rpgmakerweb.com/index.php?/topic/53552-whtdragons-animals-and-running-horses-now-with-more-dragons/

wind.png
http://biometalneo.deviantart.com/art/Water-and-Wind-204610311

Used in tile:

clock
http://4.bp.blogspot.com/-ro9o6MZddQg/ULYKmIr6qpI/AAAAAAAADgM/6yyBdVoM-1w/s1600/100.png

rpg_maker_vx_rtp_tileset_by_telles0808 (used in Tiled)
http://telles0808.deviantart.com/art/RPG-Maker-VX-RTP-Tileset-159218223

silverIV (used in Tiled)
http://opengameart.org/content/basic-map-32x32-by-silver-iv


========================FONTS USED========================
https://www.fontsquirrel.com/fonts/Green-Fuz
http://www.1001fonts.com/digital-7-font.html
https://www.fontsquirrel.com/fonts/kaushan-script


========================MUSIC/SOUND SOURCES========================

Main Music (Includes all rounds):
slumlord by lo tag blanco (c) copyright 2006 Licensed under a Creative Commons Attribution license.
http://dig.ccmixter.org/files/lotagblanco/4938

Wind Sound Effect:
	http://www.flashkit.com/soundfx/Ambience/FSWISH-Martin_B-7856/index.php
