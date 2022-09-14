import pygame

pygame.init()
FONT = pygame.font.Font('src/font/Pixeltype.ttf', 48)
SMALL_FONT = pygame.font.Font('src/font/Pixeltype.ttf', 16)

FPS = 30
WIDTH, HEIGHT = 1280, 720
TITLE = 'Wireworld'
TILE_SIZE = 50
COLORS = {
    0: 'dimgray',
    1: 'yellow',
    2: 'cyan',
    3: 'red'}