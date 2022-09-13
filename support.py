import pygame, sys
from settings import *

def exit():
    pygame.quit()
    sys.exit()

def drawText(text, color, surf, x, y, font):
    textRender = font.render(text, 1, color)
    textRect = textRender.get_rect()
    textRect.topleft = (x, y)
    surf.blit(textRender, textRect)

def save(path, iterator):
    cells = ""
    with open(path, 'w') as file:
        for row in iterator:
            line = ""
            for tile in row:
                line += str(tile.state) + " "
            cells += line + '\n'
        file.write(cells)

def load(path, tiles):
    with open(path, 'r') as file:
        y, x = 0, 0
        for row in file:
            x = 0
            line = row.split()
            for tile in line:
                tiles[y][x].state = int(tile)
                x += 1
            y += 1

class Button:
    def __init__(self, color, x, y, width, height, text = ''):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.active = True

    def draw(self, surf, color: str, ofsX: int = 0, ofsY: int = 0, small: bool = False, outline = None,):
        if not self.active:
            if outline:
                pygame.draw.rect(surf, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            pygame.draw.rect(surf, COLORS[0], (self.x, self.y, self.width, self.height), 0)
        else:
            pygame.draw.rect(surf, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            if not small:
                drawText(self.text, color, surf, self.x + ofsX, self.y + ofsY, FONT)
            else:
                drawText(self.text, color, surf, self.x + ofsX, self.y + ofsY, SMALL_FONT)

    def toggleActive(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def isActive(self):
        if self.active:
            return True
        else:
            return False

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False
