from random import randint
from global_parameters import COLUMNS, PINK, PURPLE, ROWS
from square import Square

class Apple(Square):
    def __init__(self, player_id) -> None:
        '''Skapa ett äpple'''
        super().__init__(
            randint(0, COLUMNS-1),
            randint(0, ROWS-1), 
            PINK if player_id == 1 else PURPLE
        )
        self.updated = False