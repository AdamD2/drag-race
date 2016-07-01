import pygame
from pygame.sprite import Sprite
from time import sleep

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

        # Store a decimal value for the car's left
        self.left = float(self.rect.left)

        # Movement flags
        self.accelerating = False

        # Acceleration value
        self.acceleration = 10.0

        # Time value
        self.time = 0

    def update(self):
        """Update the car's position based on the movement flag."""
        sleep(0.01)
        self.time += 0.01

        if self.accelerating and self.rect.right < self.screenRect.right:
            self.left = 0.5 * self.acceleration * self.time**2

        # Update the rect object
        self.rect.left = self.left

    def blitme(self):
        """Draw the car at its current location."""
        self.screen.blit(self.image, self.rect)
