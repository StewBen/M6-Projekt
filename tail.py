"""Contains the class for a Tail object."""

from square import Square

class Tail(Square):
    """A tail object that follows the snake head."""
    def __init__(self, x, y, hp, color):
        super().__init__(x, y, color) # Setup square 
        self.hp = hp

    def decrease_hp(self):
        """Decreases health points by one."""
        self.hp -= 1
