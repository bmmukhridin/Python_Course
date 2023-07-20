class GameStats:
    """
    Track statistics for Alien Invasion
    """
    def __init__(self,ai_game):
        """
        Initilize statistics
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # Start alien invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """
        Initilize statistics that can change during the game
        """
        self.ship_left = self.settings.ship_limit

