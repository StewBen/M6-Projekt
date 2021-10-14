"""Contains the class for a Button object."""

import pygame

class Button():
    "A clickable and customizable button."

    def __init__(self, x, y, width, height, fontsize, text=''):
        "Inits variables."
        self.x = x               # Left x
        self.y = y               # Top y
        self.width = width
        self.height = height
        self.fontsize = fontsize
        self.text = text

    def draw(self, screen):
        "Call this method to draw the button on the screen."
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (236,239,244), rect, 0) # White background

        if self.text != '':
            font = pygame.font.Font('fonts\Mario-Kart-DS.ttf', self.fontsize)
            text = font.render(self.text, True, (10,10,10))                      # Black text
            screen.blit(text, (self.x + (self.width  - text.get_width())  // 2,  # Text X-pos
                               self.y + (self.height - text.get_height()) // 2)) # Text Y-pos

    def is_over(self, pos):
        "Pos is the mouse position or a tuple of (x,y) coordinates."
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
