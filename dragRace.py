import pygame
import gameFunctions as gf
from settings import Settings
from car import Car

def runGame():
    # Initialize game, settings and screen object
    pygame.init()
    drSettings = Settings()
    screen = pygame.display.set_mode(
        (drSettings.screenWidth, drSettings.screenHeight))
    pygame.display.set_caption("Drag Race")

    # Make the car
    car = Car(drSettings, screen)

    # Initialize the timer, gear text and speed



    # Start the main loop for the game
    while True:
        # Check for keypresses
        gf.checkEvents()


        # Update the position of the car
        


        # Update the screen
        gf.updateScreen(drSettings, screen, car)


runGame()
