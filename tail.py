"""Contains the class for a Tail object."""

class Tail:
    """A tail object that follows the snake head."""
    def __init__(self, x, y, hp, color):
        self.x = x
        self.y = y
        self.color = color
        self.hp = hp

    def decrease_hp(self):
        """Decreases health points by one."""
        self.hp -= 1
