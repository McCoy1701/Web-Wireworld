import pygame

pygame.init()
FONT = pygame.font.Font('font/Pixeltype.ttf', 48)
SMALL_FONT = pygame.font.Font('font/Pixeltype.ttf', 16)

FPS = 60
WIDTH, HEIGHT = 1280, 720
TITLE = 'Wireworld'
TILE_GRID_SIZE = 50
TILE_SIZE = 50
COLORS = {
    0: 'dimgray',
    1: 'yellow',
    2: 'cyan',
    3: 'red'}