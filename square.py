from typing import Tuple
import pygame
from global_parameters import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, SQUARE_WIDTH, SQUARE_HEIGHT

class Square:
    '''Klass för en ruta i rutnätet'''

    def __init__(self, x: int, y: int, color: Tuple[int, int, int]) -> None:
        '''Skapa en ruta'''
        # Pixel koordinater för rutan (x -> längst åt vänster, y -> högst upp)
        self.x = x                      
        self.y = y

        # Index i rutnätet
        self.row_index = 0 if self.y == 0 else int(self.y / SQUARE_HEIGHT) 
        self.column_index = 0 if self.x == 0 else int(self.x / SQUARE_WIDTH)
        
        # Rutans färg
        self.color = color 
        
        # Kvadrat som pygame kan rita
        self.rect = pygame.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)
        
        # Points för att rita linje runtom rutan
        self.points = [
            (self.x, self.y),
            (self.x + SQUARE_WIDTH, self.y),
            (self.x + SQUARE_WIDTH, self.y + SQUARE_HEIGHT),
            (self.x, self.y + SQUARE_HEIGHT)
        ]

    def __repr__(self) -> str:
        '''Tjusig utskrift kanske'''
        return f"(x: {self.x}, y: {self.y})"