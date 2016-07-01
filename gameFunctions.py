import sys
import pygame

def checkEvents(car, stats):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, car, stats)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, car)

def checkKeydownEvents(event, car, stats):
    """Respond to keydown events."""
    if event.key == pygame.K_SPACE:
        # Accelerate the vehicle
        car.accelerating = True
        car.newMotion()
    elif event.key == pygame.K_UP:
        # Shift up a gear
        car.shiftUp()
    elif event.key == pygame.K_DOWN:
        # Shift down a gear
        car.shiftDown()
    elif event.key == pygame.K_RIGHT:
        # Reset the game
        if stats.gameActive == False:
            stats.gameActive = True
        elif stats.gameAction == True:
            stats.gameActive = False
    elif event.key == pygame.K_q:
        # Quit the game
        sys.exit()

def checkKeyupEvents(event, car):
    """Respond to key releases."""
    if event.key == pygame.K_SPACE:
       # Stop accelerating the vehicle
       car.accelerating = False
       car.newMotion()

def updateScreen(drSettings, screen, car, hud):
    """Update all images on the screen."""
    # Redraw the screen background
    screen.fill(drSettings.bgColor)

    # Redraw the car
    car.blitme()

    # Draw the timer, gear text and speed
    hud.showHud()

    # Make the most recently drawn screen visible
    pygame.display.flip()
