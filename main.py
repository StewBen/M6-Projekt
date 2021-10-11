"""Mall för ett pygame spel."""

### Imports:
import pygame

from global_parameters import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SPEED
from grid import Grid
from snake import Snake

def main(screen):
    """Main-funktion för spelet."""

    # Boiler plate
    pygame.init()
    clock = pygame.time.Clock() 
    move_event = pygame.USEREVENT
    pygame.time.set_timer(move_event, SPEED)

    # Gör ett grid
    grid = Grid(screen)

    # Skapa lite ormar :)
    snake1 = Snake(1)
    snake2 = Snake(2)

    ### Vår main-loop, varje iteration av loop:en = 1 frame:
    program_running = True
    winner = ''
    while program_running:
        ### Checks for keypresses:  
        keys = pygame.key.get_pressed()

        snake1.change_direction(keys)
        snake2.change_direction(keys)

        ### Kollar efter mus/tangenttryck:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == move_event:  # Every SPEED ms:
                # Kolla om man ens move gjorde så man torska
                if snake1.move(grid) == 'lost':
                    program_running = False
                    winner = 'P2'
                elif snake2.move(grid) == 'lost': # Move the snakes
                    program_running = False
                    winner = 'P1'

        if grid.drawFlag:
            grid.draw()

        clock.tick(FPS)
        pygame.display.flip()
    print(f'Winner is {winner}')

display_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Duel')

main(display_window)