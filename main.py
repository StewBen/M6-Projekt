"""Snake-Duel, a 1v1 multiplayer spin on the classic game Snake.
   Created for project module M6 by Viktor Stubbfält and Einar Johansson."""

### Imports:
from random import randint
import pygame

### Global variables:
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
FPS = 60
WIDTH = 18
GRID_SIZE = SCREEN_WIDTH // WIDTH
BLACK = (0,0,0)

def draw_grid(screen, grid):
    """Draws the contents of the playing field."""

    for x, column in enumerate(grid):
        for y, row in enumerate(column):
            square = pygame.Rect(x * WIDTH + (x * WIDTH) % 18, # Left edge position
                                 y * WIDTH + (y * WIDTH) % 18, # Top edge position
                                 WIDTH,                        # Width
                                 WIDTH)                        # Height
            pygame.draw.rect(screen, row, square)              # Does the drawing

def main(screen):
    """Main-function for the game."""

    pygame.init()               # Initiates pygame
    program_running = True      # Is the program running or not
    clock = pygame.time.Clock() # Time variable

    ### Initates the grid variable with either black or random colors:
    #grid = [[BLACK for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    grid = [[(randint(0,255),randint(0,255),randint(0,255)) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    ### Our main-loop, every iteration of the loop = 1 frame:
    while program_running:

        ### Checks for mouse/keypresses:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If you close the window
                pygame.quit()             # Quits the program
                return None               # Solves odd error

        draw_grid(screen, grid) # Draws the playing field

        clock.tick(FPS)       # Sets our target FPS
        pygame.display.flip() # The *actual* drawing of this frame

### Initiate a "display variable" to draw things on:
display_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Duel') # The title of the window

### Starts the game!
main(display_window)
