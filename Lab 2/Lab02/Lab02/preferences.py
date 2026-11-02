"""Antarctic Survival display, gameplay, and image settings.
Reconstructed from the interfaces expected by the supplied starter files.
"""
import os
import pygame


class Preferences:
    """Shared constants used by the board, controller, and cells."""
    pygame.init()
    NUM_ROWS = 12
    NUM_COLS = 16
    NUM_CELLS = NUM_ROWS * NUM_COLS
    CELL_WIDTH = 40
    CELL_HEIGHT = 40
    BOARD_WIDTH = NUM_COLS * CELL_WIDTH
    BOARD_HEIGHT = NUM_ROWS * CELL_HEIGHT + 40

    COLOR_BACKGROUND = pygame.Color('aliceblue')
    COLOR_PLAYER = pygame.Color('dodgerblue')
    COLOR_FOOD = pygame.Color('gold')
    COLOR_ENEMY = pygame.Color('firebrick')

    SCORE_FONT = pygame.font.SysFont(None, 30)
    SCORE_TEXT = 'Bands Collected: {}'
    SCORE_FONT_COLOR = pygame.Color('black')
    GAMEOVER_FONT = pygame.font.SysFont(None, 58)
    GAMEOVER_TEXT = 'Imprisoned by patrol'
    GAMEOVER_FONT_COLOR = pygame.Color('darkred')

    SLEEP_TIME = 50
    FOOD_ADD_RATE = 10
    ENEMY_ADD_RATE = 50
    MAX_FOOD = 0.25
    MAX_ENEMIES = 0.15

    IMG_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
    PLAYER_IMAGE = os.path.join(IMG_DIR, 'Headshot_me.png')
    FOOD_IMAGE = os.path.join(IMG_DIR, 'Money_wad.png')
    ENEMY_IMAGE = os.path.join(IMG_DIR, 'Boarder_Patrol.png')
