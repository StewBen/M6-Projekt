import copy
import pygame
from apple import Apple
from global_parameters import BLACK, GREEN, ORANGE
from grid import Grid
from head import Head

class Snake:
    def __init__(self, player_id: int) -> None:
        '''Skapa en orm'''
        self.player_id = player_id      # Spelarens id
        self.head = Head(player_id)     # Ormens huvud
        self.tail = []                  # Lista med gamla huvuden
        self.direction = 0              # Färdriktning
        self.tailLength = 5             # Hur många rutor i svansen
        self.apple = Apple(player_id)   # Ett äpple som ormen ska äta

    def getInfo(self):
        '''Jätteful funktion, returnerar index och färg för alla rutor i svansen (inkl. huvudet)'''
        # All info om svansen
        info = [((square.row_index, square.column_index), square.color) for square in self.tail]
        # Lägger till info om huvudet
        info += [((self.head.row_index, self.head.column_index), self.head.color)]
        return info

    def move(self, grid: Grid) -> str:
        '''Flytta ormen'''
        if not self.apple.updated:
            # Rita äpplet
            grid.setSquare(self.apple.getIndex(), self.apple.color)
            self.apple.updated = True

        # Gör en kopia av self.head och sätter den i början av svansen
        old_head = copy.deepcopy(self.head)
        old_head.color = ORANGE if self.player_id == 1 else GREEN
        self.tail.insert(0, old_head)

        # Om svansen är längre än max längden, ta bort sista och gör den svart
        if len(self.tail) > self.tailLength:
            last = self.tail.pop(len(self.tail)-1)
            grid.setSquare(last.getIndex(), BLACK)
        
        # Flytta huvudet
        self.head.move(self.direction)
        
        # Kolla om huvudet krocka
        newhead = grid.getSquare(self.head.getIndex())

        if newhead.color != BLACK:
            return 'lost'
        elif newhead.color == self.apple.color:
            # Gör svansen en square längre.
            pass
        
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