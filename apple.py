from random import randint
import pygame

### Global variables:
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
SPEED = 100 # Milliseconds between each step of snake movement
WIDTH = 18 # Width and height of all squares ingame
GRID_SIZE = SCREEN_WIDTH // WIDTH # Amount of squares for one side

class Apple:
    def __init__(self, player_id):
        self.x = randint(0, GRID_SIZE-1)
        self.y = randint(0, GRID_SIZE-1)
        self.id = player_id
        if self.id == 1:
            self.color = (150,0,0)
        else:
            self.color = (0,0,150)