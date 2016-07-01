import pygame
import gameFunctions as gf
from headUpDisplay import HeadUpDisplay
from settings import Settings
from car import Car

def runGame():
    # Initialize game, settings and screen object
    pygame.init()
    drSettings = Settings()
    screen = pygame.display.set_mode(
        (drSettings.screenWidth, drSettings.screenHeight))
    pygame.display.set_caption("Drag Race")
    totalTime = 0

    # Make the car
    car = Car(drSettings, screen)

    # Initialize the timer, gear text and speed
    hud = HeadUpDisplay(drSettings, screen, totalTime, car) 

    # Start the main loop for the game
    while True:
        # Check for keypresses
        gf.checkEvents(car)


        # Update the position of the car and the hud
        car.update() 
        hud.update(totalTime, car)
        totalTime += drSettings.timeIncrement

        # Update the screen
        gf.updateScreen(drSettings, screen, car, hud)


runGame()
