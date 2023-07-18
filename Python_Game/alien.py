import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    A class to represent a single alien in the fleet
    """
    def __init__(self, ai_game):
        """
        Initialize the alien and set its starting position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien exact horizontal position
        self.x = float(self.rect.x)


