"""Contains the class for an Apple object."""

### Imports:
from random import randint
from global_parameters import ORANGE, GREEN, GRID_SIZE

class Apple:
    """An apple that snakes hunt for to grow."""
    def __init__(self, player_id):
        self.x = randint(0, GRID_SIZE-1)
        self.y = randint(0, GRID_SIZE-1)
        self.id = player_id

        if self.id == 1:
            self.color = ORANGE
        else:
            self.color = GREEN
