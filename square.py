from typing import Tuple
import pygame
from global_parameters import SQUARE_WIDTH, SQUARE_HEIGHT

class Square:
    '''Klass för en ruta i rutnätet'''

    def __init__(self, col: int, row: int, color: Tuple[int, int, int]) -> None:
        '''Skapa en ruta'''
        # Pixel koordinater för rutan (x -> längst åt vänster, y -> högst upp)
        self.x = col * SQUARE_WIDTH
        self.y = row * SQUARE_HEIGHT

        # Index i rutnätet
        self.row_index = row
        self.column_index = col

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
        return f"(rad: {self.row_index}, kolumn: {self.column_index})"
    
    def getIndex(self) -> Tuple[int, int]:
        '''Returnera index i rutnätet'''
        return (self.row_index, self.column_index)