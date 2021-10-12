import pygame

from global_parameters import WIDTH

class Square:
    '''A square in the grid.'''
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color   

    def rect(self, row, column):
        return pygame.Rect(
                         column * WIDTH + (column * WIDTH) % WIDTH, # Left edge position
                         row * WIDTH + (row * WIDTH) % WIDTH,       # Top edge position
                         WIDTH, WIDTH)                              # Width, height
