class GameStats():
    """Track statistics and high scores."""

    def __init__(self):
        """Initialize high score stats."""

        # Start game in an inactive state
        self.gameActive = False

        # Store the high score
        self.highScore = 0

        self.resetStats()

    def resetStats(self):
        """Initialize stats that may be reset."""
        self.totalTime = 0
