"""Contains the class for a Grid object."""

### Imports:
import pygame
from square import Square
from tail import Tail
from apple import Apple
from global_parameters import RED, BLUE, GRID_SIZE

class Snake(Square):
    """A snake to be controlled by a player."""
    def __init__(self, x, y, player_id):
        color = RED if player_id == 1 else BLUE
        super().__init__(x, y, color) # Setup square 
        self.player_id = player_id
        self.direction = 0
        self.length = 0
        self.tails = []
        self.apple = Apple(self.player_id, self.getSquares())
        self.moved = False

    def move(self):
        """Move the snake by 1 step. 0 = up, 1 = right, 2 = down, 3 = left."""

        self.move_tail()

        ### Moves head:
        if not self.moved:
            if self.direction == 0:
                self.y -= 1
            elif self.direction == 1:
                self.x += 1
            elif self.direction == 2:
                self.y += 1
            elif self.direction == 3:
                self.x -= 1
        self.moved = True

        self.apple_collision()
    
    def getSquares(self):
        '''Returnerar en lista med ormens squares (inkl. huvudet)'''
        squares = [tail for tail in self.tails]
        squares.append(Square(self.x, self.y, self.color))
        return squares

    def move_tail(self):
        """Move the chain of tails forward one position."""

        ### Removes last tail:
        for tail in self.tails:
            tail.decrease_hp()
            self.tails = [x for x in self.tails if not x.hp == 0]

        ### Creates new first tail:
        if self.length > 0:
            self.tails.append(Tail(self.x, self.y, self.length, self.color))

    def wall_collision(self):
        """Checks if the snake has hit a wall."""
        if self.x < 0 or self.y < 0:
            return True
        if self.x >= GRID_SIZE or self.y >= GRID_SIZE:
            return True

    def apple_collision(self):
        """Checks for apple collision, if collision: adds a tail and a new apple."""
        if self.x == self.apple.x and self.y == self.apple.y:
            self.length += 1
            self.apple = Apple(self.player_id, self.getSquares())

    def snake_collision(self, other_snake):
        '''Check if we have bumped into another snake'''
        squares = other_snake.getSquares()

        for square in squares:
            if square.x == self.x and square.y == self.y:
                return True
        return False

    def tail_collision(self):
        '''Returnerar om huvudet har krockat med sin svans'''
        for tail in self.tails:
            if tail.x == self.x and tail.y == self.y:
                return True
        return False

    def change_direction(self, keys):
        """Changes the direction of the snake head.
           Player 1: WASD controls
           Player 2: Arrow key controls"""

        if self.player_id == 1:
            if keys[pygame.K_w] and self.direction != 2:
                self.direction = 0
            if keys[pygame.K_d] and self.direction != 3:
                self.direction = 1
            if keys[pygame.K_s] and self.direction != 0:
                self.direction = 2
            if keys[pygame.K_a] and self.direction != 1:
                self.direction = 3

        elif self.player_id == 2:
            if keys[pygame.K_UP] and self.direction != 2:
                self.direction = 0
            if keys[pygame.K_RIGHT] and self.direction != 3:
                self.direction = 1
            if keys[pygame.K_DOWN] and self.direction != 0:
                self.direction = 2
            if keys[pygame.K_LEFT] and self.direction != 1:
                self.direction = 3
