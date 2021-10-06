"""Contains the class for a Snake object."""

import pygame

BLACK = (0,0,0)

class Grid:
    """Color data stored in a grid."""
    def __init__(self, size, width):
        self.size = size
        self.width = width
        self.data = [[BLACK for _ in range(self.size)] for _ in range(self.size)]

    def reset(self):
        """Resets all grid data to black color."""
        self.data = [[BLACK for _ in range(self.size)] for _ in range(self.size)]

    def update(self, player_1):
        """Updates the data of grid."""
        self.data[player_1.x][player_1.y] = player_1.color

    def draw(self, screen):
        """Draws the contents of the playing field."""
        for x, column in enumerate(self.data):
            for y, row in enumerate(column):
                square = pygame.Rect(
                         x * self.width + (x * self.width) % self.width, # Left edge position
                         y * self.width + (y * self.width) % self.width, # Top edge position
                         self.width, self.width)                         # Width, height
                pygame.draw.rect(screen, row, square)                    # Draws the square
