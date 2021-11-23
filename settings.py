
class Settings():
    """"A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 1200
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_limit = 3

        # Bullets settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 6

        # Alien settings
        self.fleet_drop_speed = 10
        

        # Speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize variable settings."""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direcion of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)