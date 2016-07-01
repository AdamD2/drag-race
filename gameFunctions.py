import sys
import pygame

def checkEvents():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event)

def checkKeydownEvents(event):
    """Respond to keydown events."""
    if event.key == pygame.K_SPACE:
        # Accelerate the vehicle
        pass
    elif event.key == pygame.K_LEFT:
        # Shift up a gear
        pass
    elif event.key == pygame.K_RIGHT:
        # Reset the game
        pass
    elif event.key == pygame.K_q:
        # Quit the game
        sys.exit()

def updateScreen():
    # Draw the car and text on the screen
    pass
