import pygame
from pygame.sprite import Sprite

class Car(Sprite):
    """A class to model and move the dragster."""

    def __init__(self, drSettings, screen):
        """Initialize the car and set its position."""
        super(Car, self).__init__()
        self.screen = screen
        self.drSettings = drSettings

        # Load in the car image
        self.image = pygame.image.load('images/car.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # Start the car at the center left of the screen
        self.rect.left = self.screenRect.left
        self.rect.centery = self.screenRect.centery

        # Store a decimal value for the car's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.accelerating = False
