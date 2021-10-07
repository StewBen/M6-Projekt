"""Contains the class for a Grid object."""

### Imports:
import pygame
from global_parameters import WHITE, BLACK

class Grid:
    """Color data stored in a grid."""
    def __init__(self, squares, width, size):
        self.squares = squares
        self.width = width
        self.size = size
        self.data = [[BLACK for _ in range(self.squares)] for _ in range(self.squares)]

    def reset(self):
        """Resets all grid data to black color."""
        self.data = [[BLACK for _ in range(self.squares)] for _ in range(self.squares)]

    def update(self, player_1):
        """Updates the data of grid."""
        self.data[player_1.x][player_1.y] = player_1.color
        self.data[player_1.apple.x][player_1.apple.y] = player_1.apple.color
        for tail in player_1.tails:
            self.data[tail.x][tail.y] = tail.color

    def draw_squares(self, screen):
        """Draws the squares of the playing field."""
        for x, column in enumerate(self.data):
            for y, row in enumerate(column):
                square = pygame.Rect(
                         x * self.width + (x * self.width) % self.width, # Left edge position
                         y * self.width + (y * self.width) % self.width, # Top edge position
                         self.width, self.width)                         # Width, height
                pygame.draw.rect(screen, row, square)                    # Draws the square

    def draw_lines(self, screen):
        """Draws grid lines on the playing field."""
        for i, _ in enumerate(self.data):
            pygame.draw.line(screen, WHITE, (i * self.width, 0), (i * self.width, self.size))
            pygame.draw.line(screen, WHITE, (0, i* self.width), (self.size, i * self.width))
