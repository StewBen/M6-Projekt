"""Snake-Duel, a 1v1 multiplayer spin on the classic game Snake.
   Created for project module M6 by Viktor Stubbfält and Einar Johansson."""

### Imports:
import pygame
from snake import Snake
from grid import Grid
from menu import gameover
from button import Button
from global_parameters import SCREEN_WIDTH, SCREEN_HEIGHT, WIDTH, GRID_SIZE

def main(screen):
    """Main-function for the game."""
    pygame.init()                 # Initiates pygame
    pygame.font.init()            # Inits font handling
    program_running = True        # Is the program running or not
    grid = Grid(GRID_SIZE, WIDTH, SCREEN_WIDTH) # Initates the grid variable with black colors
    player_1 = Snake(12, 12, 1)   # Player 1

    SPEED = 300
    ACCELERATION = 5000
    clock = pygame.time.Clock()
    stopwatch = 0

    ### Sets up an event every ACCELERATION ms to increase snake speed:
    accelerate_event = pygame.USEREVENT
    pygame.time.set_timer(accelerate_event, ACCELERATION)

    ### Our main-loop, every iteration of the loop = 1 frame:
    while program_running:

        ### Adds time since last frame to stopwatch:
        stopwatch += clock.get_time()

        ### Checks for keypresses:
        keys = pygame.key.get_pressed()
        player_1.change_direction(keys)

        ### Checks for game events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If you close the window
                pygame.quit()             # Quits the program
                return None               # Solves odd error

            ### Accelerates the snake:
            if event.type == accelerate_event:
                SPEED -= 10

        if stopwatch > SPEED: # Every SPEED ms:
            player_1.move()   # Move the snakes
            stopwatch = 0     # Reset stopwatch
            if player_1.wall_collision() or player_1.tail_collision():
                break

            ### Resets, updates, and then draws the playing field:
            grid.reset()
            grid.update(player_1)
            grid.draw_squares(screen)
            grid.draw_lines(screen)

            ### TEMP BUTTON TEST:
            test = Button(50, 50, 300, 100, 70, 'test123')
            test.draw(screen)

        ### The *actual* rendering of this frame:
        pygame.display.flip()
        clock.tick(60)

    gameover(screen)
    pygame.display.flip()
    pygame.time.delay(2000) # Visar gameover-skärmen i 2 sek

### Initiate a "display variable" to draw things on:
display_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Duel') # The title of the window

### Starts the game!
main(display_window)
