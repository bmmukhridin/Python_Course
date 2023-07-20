# Settings
class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """
        Initialize the game's settings
        """
        # Screen settings
        self.screen_width = 800
        self.screen_height = 1200

        # ship settings
        self.ship_speed = 0.6
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (39,145,50)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1


