from random import randint
from typing import List, Tuple
import copy
import pygame
from global_parameters import BLACK, BLUE, COLUMNS, ORANGE, RED, ROWS, SQUARE_HEIGHT, SQUARE_WIDTH, WHITE
from grid import Grid
from square import Square

class Snake:
    def __init__(self, player_id: int) -> None:
        '''Skapa en orm'''
        self.player_id = player_id      # Spelarens id
        self.head = Head(player_id)     # Ormens huvud
        self.tail = []                  # Lista med gamla huvuden
        self.direction = 0              # Färdriktning
        self.tailLength = 5             # Hur många rutor i svansen

    def getInfo(self):
        '''Jätteful funktion, returnerar index och färg för alla rutor i svansen (inkl. huvudet)'''
        # All info om svansen
        info = [((square.row_index, square.column_index), square.color) for square in self.tail]
        # Lägger till info om huvudet
        info += [((self.head.row_index, self.head.column_index), self.head.color)]
        return info

    def move(self, grid: Grid) -> str:
        '''Flytta ormen'''
        # Gör en kopia av self.head och sätter den i början av svansen
        old_head = copy.deepcopy(self.head)
        old_head.color = ORANGE
        self.tail.insert(0, old_head)

        # Om svansen är längre än max längden, ta bort sista och gör den svart
        if len(self.tail) > self.tailLength:
            last = self.tail.pop(len(self.tail)-1)
            grid.setSquare(last.getIndex(), BLACK)
        
        # Flytta huvudet
        self.head.move(self.direction)
        
        # Kolla om huvudet krocka
        newhead = grid.getSquare(self.head.getIndex())

        if newhead.color != BLACK: # Uppdatera för äpplen
            return 'lost'
        
        # Uppdatera grid
        self.update_grid(grid)

    def change_direction(self, keys) -> None:
        '''Ändra färdriktningen för ormen'''
        if self.player_id == 1:
            if keys[pygame.K_w] and self.direction != 2:
                self.direction = 0
            if keys[pygame.K_d] and self.direction != 3:
                self.direction = 1
            if keys[pygame.K_s] and self.direction != 0:
                self.direction = 2
            if keys[pygame.K_a] and self.direction != 1:
                self.direction = 3
        else:
            if keys[pygame.K_UP] and self.direction != 2:
                self.direction = 0
            if keys[pygame.K_RIGHT] and self.direction != 3:
                self.direction = 1
            if keys[pygame.K_DOWN] and self.direction != 0:
                self.direction = 2
            if keys[pygame.K_LEFT] and self.direction != 1:
                self.direction = 3

    def update_grid(self, grid: Grid):
        '''Uppdatera ormens rutor i rutnätet'''
        for info in self.getInfo():
            index = info[0]
            color = info[1]
            grid.setSquare(index, color)

class Head:
    '''Klass för huvudet på ormen'''
    def __init__(self, player_id) -> None:
        '''Skapa ett huvud'''

        # Vart i rutnätet huvudet ligger
        self.row_index = randint(0, ROWS-1)
        self.column_index = randint(0, COLUMNS-1)

        # Huvudets färg
        self.color = RED if player_id == 1 else BLUE

    def move(self, direction: int) -> None:
        '''Flytta huvudet i given riktning'''
        if direction == 0:
            self.row_index -= 1
        elif direction == 1:
            self.column_index += 1
        elif direction == 2:
            self.row_index += 1
        elif direction == 3:
            self.column_index -= 1

        # Förhindrar out of bounds error
        self.row_index %= ROWS
        self.column_index %= COLUMNS

    def getIndex(self) -> Tuple[int, int]:
        '''Returnera index i rutnätet för huvudet'''
        return (self.row_index, self.column_index)