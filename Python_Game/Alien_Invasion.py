# Alien_Invasion
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """
    Overall class to manage game assets and behavior
    """
    def __init__(self):
        """
        Initialize the gane, and create game resources
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Allien Invension")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set the color background color.
        # self.bg_color(230, 230, 230)

    def run_game(self):
        """
        Start the main loop for the game
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            # print(len(self.bullets))
            
            
            
    def _check_events(self):
        """
        Respond to keypress and mouse events
        """
        # Watch for keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)

            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    
    def _update_screen(self):
        """
        Update image on the screen, and flip to the new screen
        """
        # Redraw the screen during each pass through the loop
        self.screen.fill((230,230,230))
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_key_down(self, event):
        """
        Respond to keypress
        """
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up(self, event):
        """
        Respond to key releases
        """
        if event.key == pygame.K_RIGHT:
            # Stop the ship to the right turn
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop the ship to the left turn
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid if old bulets"""
        # update bullet position

if __name__ == "__main__":
     # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()