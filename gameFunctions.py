import sys
import pygame

def checkEvents(car):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, car)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, car)

def checkKeydownEvents(event, car):
    """Respond to keydown events."""
    if event.key == pygame.K_SPACE:
        # Accelerate the vehicle
        car.accelerating = True
    elif event.key == pygame.K_LEFT:
        # Shift up a gear
        pass
    elif event.key == pygame.K_RIGHT:
        # Reset the game
        pass
    elif event.key == pygame.K_q:
        # Quit the game
        sys.exit()

def checkKeyupEvents(event, car):
    """Respond to key releases."""
    if event.key == pygame.K_SPACE:
       # Stop accelerating the vehicle
       car.accelerating = False

def updateScreen(drSettings, screen, car):
    """Update all images on the screen."""
    # Redraw the screen background
    screen.fill(drSettings.bgColor)

    # Redraw the car
    car.blitme()

    # Draw the timer, gear text and speed


    # Make the most recently drawn screen visible
    pygame.display.flip()
