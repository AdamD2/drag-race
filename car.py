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

        self.initializeDynamicSettings()

    def initializeDynamicSettings(self):
        """Initialize settings that change so that they can be reset."""
        self.accelerating = False
        self.acceleration = self.drSettings.acceleration[0]
        self.time = 0
        self.gear = 0
        self.velocity = 0
        self.initialVelocity = 0
        self.initialPos = 0

    def update(self):
        """Update the car's position based on the movement flag."""
        sleep(0.01)
        self.time += 0.01

        self.velocity = self.acceleration * self.time

        if self.accelerating and self.rect.right < self.screenRect.right:
            self.left = (self.initialPos + self.initialVelocity * self.time
                + 0.5 * self.acceleration * self.time**2)

#        if self.velocity > self.drSettings.speedCap[self.gear]:
#            self.acceleration = 0
#        else:
#            self.acceleration = self.drSettings.acceleration[self.gear]

        # Update the rect object
        self.rect.left = self.left

    def shiftUp(self):
        """Move up a gear, with lower acceleration but higher speed."""
        if self.gear < 5:
            self.gear += 1
            self.acceleration = self.drSettings.acceleration[self.gear] 
            self.initialVelocity = self.velocity
            self.initialPos = self.rect.left
            self.time = 0

    def shiftDown(self):
        """Move down a gear, with higher acceleration but lower speed."""
        if self.gear > 0:
            self.gear -= 1
            self.acceleration = self.drSettings.acceleration[self.gear]
            self.initialVelocity = self.velocity
            self.initialPos = self.rect.left
            self.time = 0

    def blitme(self):
        """Draw the car at its current location."""
        self.screen.blit(self.image, self.rect)
