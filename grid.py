"""Contains the class for a Grid object."""

### Imports:
import pygame
from global_parameters import WHITE, BLACK
from square import Square
class Grid:
    """Color data stored in a grid."""
    def __init__(self, squares, width, size):
        self.squares = squares
        self.width = width
        self.size = size
        
        self.reset()

    def reset(self):
        """Resets all grid data to black color."""
        self.data = [[Square(col * self.width, row * self.width, BLACK) for col in range(self.squares)] for row in range(self.squares)]
    
    def update(self, player_1):
        """Updates the data of grid."""

        self.data[player_1.x][player_1.y] = player_1
        self.data[player_1.apple.x][player_1.apple.y] = player_1.apple
        for tail in player_1.tails:
            self.data[tail.x][tail.y] = tail

    def draw_squares(self, screen):
        """Draws the squares of the playing field."""
        for x, column in enumerate(self.data):
            for y, row in enumerate(column):                
                pygame.draw.rect(screen, row.color, row.rect(y, x)) # Draws the square

    def draw_lines(self, screen):
        """Draws grid lines on the playing field."""
        for i, col in enumerate(self.data):
            pygame.draw.line(screen, WHITE, (i * self.width, 0), (i * self.width, self.size))
            pygame.draw.line(screen, WHITE, (0, i* self.width), (self.size, i * self.width))
