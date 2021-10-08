"""Contains the class for an Apple object."""

### Imports:
from random import randint
from global_parameters import ORANGE, GREEN, GRID_SIZE
from square import Square

class Apple(Square):
    """An apple that snakes hunt for to grow."""
    def __init__(self, player_id):
        x = randint(0, GRID_SIZE-1)
        y = randint(0, GRID_SIZE-1)
        color = ORANGE if player_id == 1 else GREEN
        super().__init__(x, y, color) # Setup square 

        self.id = player_id
