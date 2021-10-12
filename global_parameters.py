"""Contains constants that are used in the entire game."""

### Game settings:
SCREEN_HEIGHT = 720
SCREEN_WIDTH = SCREEN_HEIGHT
WIDTH = 30 # Width and height of all squares ingame
GRID_SIZE = SCREEN_WIDTH // WIDTH # Amount of squares for one side
SPEED = 200 # Milliseconds between each step of snake movement

### Colors:
BLACK = (46,52,64)
WHITE = (59,66,82)
RED = (191,97,106)
BLUE = (94,129,172)
ORANGE = (208,135,112)
GREEN = (143,188,187)

# Command for call_graph:
# pyan3 apple.py global_parameters.py grid.py main.py snake.py tail.py --uses --no-defines --colored --nested-groups  --html > myuses.html
