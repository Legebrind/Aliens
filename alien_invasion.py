import pygame, sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    fondo = pygame.image.load('Images/fondo.jpg')
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create game statistics and sb
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Jugar!")

    # Start the main loop for the game.
    while True:

        gf.update_screen(ai_settings, screen, stats, sb,
            ship, aliens, bullets, play_button, fondo)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) 
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)      
            gf.update_screen(ai_settings, screen, stats, sb,
                ship, aliens, bullets, play_button, fondo)
        

run_game()


