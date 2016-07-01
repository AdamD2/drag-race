import pygame.font
from pygame.sprite import Group

class HeadUpDisplay():
    """A class to display information to the user."""

    def __init__(self, drSettings, screen, totalTime, car):
        """Initialize attributes."""
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.drSettings = drSettings

        # Font settings for information
        self.textColor = (90, 90, 90)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial images
        self.prepTime(totalTime)
        self.prepGear(car)
        self.prepVelocity(car)

    def prepTime(self, totalTime):
        """Turn the timer into a rendered image."""
        timeStr = str(round(totalTime, 2))
        self.timeImage = self.font.render(timeStr, True, self.textColor, 
            self.drSettings.bgColor)

        # Display the timer 1/4 into the screen
        self.timeRect = self.timeImage.get_rect()
        self.timeRect.centerx = int(0.25 * self.screenRect.right)
        self.timeRect.bottom = self.screenRect.height

    def prepGear(self, car):
        """Turn the gear into a rendered image."""
        gearStr = str(car.gear)
        if gearStr == "0":
            gearStr = "N"

        self.gearImage = self.font.render(gearStr, True, self.textColor,
            self.drSettings.bgColor)

        # Display the gear 1/2 into the screen
        self.gearRect = self.gearImage.get_rect()
        self.gearRect.centerx = int(0.5 * self.screenRect.right)
        self.gearRect.bottom = self.screenRect.height

    def prepVelocity(self, car):
        """Turn the velocity into a rendered image."""
        velocityStr = str(round(car.velocity, 2))
        self.velocityImage = self.font.render(velocityStr, True, self.textColor,
            self.drSettings.bgColor)

        # Display the velocity 3/4 into the screen
        self.velocityRect = self.velocityImage.get_rect()
        self.velocityRect.centerx = int(0.75 * self.screenRect.right)
        self.velocityRect.bottom = self.screenRect.height

    def update(self, totalTime, car):
        self.prepTime(totalTime)
        self.prepGear(car)
        self.prepVelocity(car)

    def showHud(self):
        """Draw the hud onto the screen."""
        self.screen.blit(self.timeImage, self.timeRect)
        self.screen.blit(self.gearImage, self.gearRect)
        self.screen.blit(self.velocityImage, self.velocityRect)
