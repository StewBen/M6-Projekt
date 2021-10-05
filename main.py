"""Mall för ett pygame spel."""

### Imports:
import pygame

### Program parameters:
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
FPS = 60

def main(screen):
    """Main-funktion för spelet."""

    pygame.init()               # Initierar pygame
    program_running = True      # Om programmet körs eller ej
    clock = pygame.time.Clock() # Tidsvariabel för FPS t.ex.

    ### Vår main-loop, varje iteration av loop:en = 1 frame:
    while program_running:

        ### Kollar efter mus/tangenttryck:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Om man kryssar fönstret
                pygame.quit()             # Stänger programmet
                return None               # Löser en märklig bugg

        screen.fill((0,0,0))  # Ritar svart bakgrund

        clock.tick(FPS)       # Sätter vår target FPS
        pygame.display.flip() # Faktiska ritningen av denna frame

### Initiera en "displayvariabel" att rita saker på:
display_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('') # Fönstrets titel

main(display_window)           # Startar spelet
