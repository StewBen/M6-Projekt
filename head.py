from random import randint
from global_parameters import BLUE, COLUMNS, RED, ROWS
from square import Square

class Head(Square):
    '''Klass för huvudet på ormen'''
    def __init__(self, player_id) -> None:
        '''Skapa ett huvud'''
        super().__init__(
            randint(0, COLUMNS-1),
            randint(0, ROWS-1), 
            RED if player_id == 1 else BLUE
        )

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