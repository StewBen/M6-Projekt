"""Functions for drawing UI elements"""

import pygame 
from global_parameters import SCREEN_HEIGHT, SCREEN_WIDTH
from button import Button

def gameover(screen, mode, winner):
    '''Ritar en gameover skärm och returnerar en knapp som användaren kan klicka på för att starta om'''
    text = ''

    # Bestäm vad gameover texten ska säga
    if mode == '1p':
        text = 'Game over'
    elif mode == '2p':
        if winner != 0:
            text = f'Player {winner} won!'
        else:
            text = 'Tie!'

    textsurface = header(text, (255, 0, 0))

    screen.blit(
        textsurface,
        (
            (SCREEN_WIDTH - pygame.Surface.get_width(textsurface)) // 2,
            (SCREEN_HEIGHT - pygame.Surface.get_height(textsurface)) // 2
        )
    )        
    
    # Knapp för att starta om
    restart = Button(
        (SCREEN_WIDTH - pygame.Surface.get_width(textsurface)) // 2,
        (SCREEN_HEIGHT - pygame.Surface.get_height(textsurface)) // 1.5,
        pygame.Surface.get_width(textsurface),
        pygame.Surface.get_height(textsurface),
        40,
        'Starta om?'
    )
    restart.draw(screen)

    pygame.display.flip()
    return restart

def header(text, color):
    font = pygame.font.Font("fonts\comic.ttf", 60)
    return font.render(text, True, color)
