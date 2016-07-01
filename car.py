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
        self.onScreen = True

    def update(self):
        """Update the car's position based on the movement flag."""
        sleep(self.drSettings.timeIncrement)
        self.time += self.drSettings.timeIncrement

        self.onScreen = self.rect.right < self.screenRect.right

        if self.accelerating and self.onScreen:
            self.left = (self.initialPos + self.initialVelocity * self.time
                + 0.5 * self.drSettings.acceleration[self.gear] * self.time**2)
            self.velocity = (self.initialVelocity + 
                self.drSettings.acceleration[self.gear] * self.time)

        peakVelocity = self.velocity > self.drSettings.speedCap[self.gear]

        if not self.accelerating and self.onScreen and self.velocity > 0:
            self.left = (self.initialPos + self.initialVelocity * self.time
                + 0.5 * self.drSettings.friction * self.time**2)
            self.velocity = (self.initialVelocity + 
                self.drSettings.friction * self.time)

#        if self.velocity > self.drSettings.speedCap[self.gear]:
#            self.acceleration = 0
#        else:
#            self.acceleration = self.drSettings.acceleration[self.gear]

        # Update the rect object
        self.rect.left = self.left

    def newMotion(self):
        self.initialVelocity = self.velocity
        self.initialPos = self.rect.left
        self.time = 0

    def shiftUp(self):
        """Move up a gear, with lower acceleration but higher speed."""
        if self.gear < 5:
            self.gear += 1
            self.initialVelocity = self.velocity
            self.initialPos = self.rect.left
            self.time = 0

    def shiftDown(self):
        """Move down a gear, with higher acceleration but lower speed."""
        if self.gear > 0:
            self.gear -= 1
            self.initialVelocity = self.velocity
            self.initialPos = self.rect.left
            self.time = 0

    def blitme(self):
        """Draw the car at its current location."""
        self.screen.blit(self.image, self.rect)
