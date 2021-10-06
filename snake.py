"""Contains the class for a Grid object."""

import pygame

RED = (255,0,0)
BLUE = (0,0,255)

class Snake:
    """A snake to be controlled by a player."""
    def __init__(self, x, y, player_id):
        self.x = x
        self.y = y
        self.player_id = player_id
        self.direction = 0
        self.tail = []
        if self.player_id == 1:
            self.color = RED
        else:
            self.color = BLUE

    def move(self):
        """Move the snake head by 1 step.
        0 = up, 1 = right, 2 = down, 3 = left."""

        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1

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
