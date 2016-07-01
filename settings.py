class Settings():
    """A class to store all settings for drag race."""

    def __init__(self):
        """Initialize static settings."""
        # Screen settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (255, 255, 255)

        # Car settings
        self.acceleration = [0, 60, 40, 20, 10, 5]
        self.speedCap = [10, 10, 40, 70, 100, 150]
        self.friction = -5

        # Timing settings
        self.timeIncrement = 0.01
