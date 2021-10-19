import pygame
from button import Button

class Main_menu():
    """Draws the main menu"""

    single_button = Button(200, 200, 200, 100, 60, 'Singleplayer')
    multi_button = Button(200, 500, 200, 100, 60, 'Multiplayer')