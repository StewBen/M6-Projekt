"""Functions for drawing UI elements"""

import pygame 
from global_parameters import SCREEN_HEIGHT, SCREEN_WIDTH

def gameover(screen):
    myfont = pygame.font.Font("fonts\comic.ttf", 60)
    textsurface = myfont.render('Game Over', True, (255, 0, 0))
    screen.blit(textsurface,((SCREEN_WIDTH - pygame.Surface.get_width(textsurface)) // 2,
                            (SCREEN_HEIGHT - pygame.Surface.get_height(textsurface)) // 2))
