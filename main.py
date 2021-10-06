"""Snake-Duel, a 1v1 multiplayer spin on the classic game Snake.
   Created for project module M6 by Viktor Stubbfält and Einar Johansson."""

### Imports:
import pygame
from snake import Snake
from grid import Grid

### Global variables:
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
SPEED = 100 # Milliseconds between each step of snake movement
WIDTH = 18 # Width and height of all squares ingame
GRID_SIZE = SCREEN_WIDTH // WIDTH # Amount of squares for one side

def main(screen):
    """Main-function for the game."""

    pygame.init()                 # Initiates pygame
    program_running = True        # Is the program running or not
    grid = Grid(GRID_SIZE, WIDTH) # Initates the grid variable with black colors
    player_1 = Snake(20, 20, 1)   # Player 1

    ### Sets up an event every SPEED ms to move the snakes:
    move_event = pygame.USEREVENT
    pygame.time.set_timer(move_event, SPEED)

    ### Our main-loop, every iteration of the loop = 1 frame:
    while program_running:

        ### Checks for keypresses:
        keys = pygame.key.get_pressed()
        player_1.change_direction(keys)

        ### Checks for game events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If you close the window
                pygame.quit()             # Quits the program
                return None               # Solves odd error

            if event.type == move_event:  # Every SPEED ms:
                player_1.move()           # Move the snakes

        ### Resets, updates, and then draws the playing field:
        grid.reset()
        grid.update(player_1)
        grid.draw(screen)

        ### The *actual* drawing of this frame:
        pygame.display.flip()

### Initiate a "display variable" to draw things on:
display_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Duel') # The title of the window

### Starts the game!
main(display_window)
