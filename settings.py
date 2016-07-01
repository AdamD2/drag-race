class Settings():
    """A class to store all settings for drag race."""

    def __init__(self):
        """Initialize static settings."""
        # Screen settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (255, 255, 255)

        self.acceleration = [0, 50, 40, 30, 20, 10]
        self.speedCap = [10, 10, 40, 70, 100, 150]
