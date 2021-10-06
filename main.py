"""Snake-Duel, a 1v1 multiplayer spin on the classic game Snake.
   Created for project module M6 by Viktor Stubbfält and Einar Johansson."""

### Imports:
import pygame

### Global variables:
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
FPS = 60
SPEED = 100 # Milliseconds between each step of snake movement
WIDTH = 18 # Width and height of all squares ingame
GRID_SIZE = SCREEN_WIDTH // WIDTH # Amount of squares for one side

### Global colors:
BLACK = (0,0,0)
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
        if self.player_id == 0:
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

def reset_grid():
    """Resets all grid data to black color."""
    return [[BLACK for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def update_grid(grid, player_1):
    """Updates the data of grid."""
    grid[player_1.x][player_1.y] = player_1.color

def draw_grid(screen, grid):
    """Draws the contents of the playing field."""
    for x, column in enumerate(grid):
        for y, row in enumerate(column):
            square = pygame.Rect(x * WIDTH + (x * WIDTH) % WIDTH, # Left edge position
                                 y * WIDTH + (y * WIDTH) % WIDTH, # Top edge position
                                 WIDTH, WIDTH)                    # Width, height
            pygame.draw.rect(screen, row, square)                 # Does the drawing

def main(screen):
    """Main-function for the game."""

    pygame.init()               # Initiates pygame
    program_running = True      # Is the program running or not
    grid = reset_grid           # Initates the grid variable with black colors
    player_1 = Snake(20, 20, 1) # Player 1

    ### Sets up an event every SPEED ms to move the snakes:
    move_event = pygame.USEREVENT
    pygame.time.set_timer(move_event, SPEED)

    ### Our main-loop, every iteration of the loop = 1 frame:
    while program_running:

        ### Checks for keypresses:
        keys = pygame.key.get_pressed()
        player_1.change_direction(keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If you close the window
                pygame.quit()             # Quits the program
                return None               # Solves odd error
    
            if event.type == move_event:  # Every SPEED ms:
                player_1.move()           # Move the snakes

        ### Resets, updates, and draws the playing field:
        grid = reset_grid()
        update_grid(grid, player_1)
        draw_grid(screen, grid)

        pygame.display.flip() # The *actual* drawing of this frame

### Initiate a "display variable" to draw things on:
display_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Duel') # The title of the window

### Starts the game!
main(display_window)
