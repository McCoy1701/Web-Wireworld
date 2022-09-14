import pygame
from src.settings import *

class Tile:
    def __init__(self, x, y, surf, tileSize):
        super().__init__()
        self.x = x
        self.y = y
        self.displaySurf = surf
        self.size = tileSize
        self.state = 0
        self.moveX = 0
        self.moveY = 0

    def draw(self, moveX, moveY):
        self.moveX = moveX
        self.moveY = moveY
        if self.x * self.size + self.moveX < 0 - self.size or self.y * self.size + self.moveY < 0 - self.size or self.x * self.size + self.moveX > \
                self.displaySurf.get_size()[0] + 5 or self.y * self.size + self.moveY > self.displaySurf.get_size()[1] + 5:
            pass
        else:
            pygame.draw.rect(self.displaySurf, COLORS[self.state],
                               pygame.Rect((self.x * self.size + moveX, self.y * self.size + moveY), (self.size - 1, self.size - 1)))
