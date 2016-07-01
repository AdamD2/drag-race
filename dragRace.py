import pygame
import gameFunctions as gf
from headUpDisplay import HeadUpDisplay
from settings import Settings
from car import Car
from gameStats import GameStats

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

    # Store the game statistics
    stats = GameStats()

    # Start the main loop for the game
    while True:
        # Check for keypresses
        gf.checkEvents(car, stats)

        # Update the game active state
        if not car.onScreen:
            stats.gameActive = False

        if stats.gameActive:
            # Update the position of the car and the hud
            car.update() 
            hud.update(stats.totalTime, car)
            stats.totalTime += drSettings.timeIncrement

        # Update the screen
        gf.updateScreen(drSettings, screen, car, hud)


runGame()
