from typing import List, Tuple
from pygame import Surface
import pygame
from square import Square
from global_parameters import COLUMNS, ROWS, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, SQUARE_HEIGHT, SQUARE_WIDTH, WHITE

class Grid:
    def __init__(self, screen: Surface) -> None:
        self.squares = self.createGrid()
        self.screen = screen
        self.drawFlag = True

    def createGrid(self) -> List[List[Square]]:
        '''Gör en 2d-lista med alla squares'''
        return [[Square(col, row, BLACK) for col in range(COLUMNS)] for row in range(ROWS)]

    def draw(self) -> None:
        '''Rita alla squares'''
        for row in self.squares:
            for square in row:
                pygame.draw.rect(self.screen, square.color, square.rect)
                pygame.draw.lines(self.screen, WHITE, True, square.points)

        self.drawFlag = False

    def setSquare(self, index: Tuple[int, int], color: Tuple[int, int, int]) -> None:
        self.getSquare(index).color = color
        self.drawFlag = True

    def getSquare(self, index: Tuple[int, int]):
        return self.squares[index[0]][index[1]]