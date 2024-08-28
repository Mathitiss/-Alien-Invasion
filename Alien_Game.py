import pygame
import sys
from settings import Settings
from ship import Ship
from enemy import Enemy
from bullet import Bullet
from bullet2 import Bullet2

class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.settings = Settings()
 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_bullets2()
            self._update_enemy()                    
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_f:
            self._fire_bullet2()

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect1.bottom <= 0 and bullet.rect2.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

    def _fire_bullet2(self):
        if len(self.bullets2) < self.settings.bullets2_allowed:
            new_bullet2 = Bullet2(self)
            self.bullets2.add(new_bullet2)

    def _update_bullets2(self):
        self.bullets2.update()

        for bullet2 in self.bullets2.copy():
            if bullet2.rect3.right >= 0 and bullet2.rect4.left <= 0:
                self.bullets2.remove(bullet2)

        collisions2 = pygame.sprite.groupcollide(self.bullets2, self.enemies, True, True)

    def _create_fleet(self):
        enemy = Enemy(self)

        enemy_width, enemy_heigh = enemy.rect.size
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemy_x = available_space_x // (2 * enemy_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * enemy_heigh) - ship_height)
        number_rows = available_space_y // (2 * enemy_heigh)
        
        for row_number in range(number_rows):
            for enemy_number in range(number_enemy_x):
                self._create_enemy(enemy_number, row_number)

    def _check_fleet_edges(self):
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_enemy(self, enemy_number, row_number):
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
        self.enemies.add(enemy)

    def _update_enemy(self):
        self._check_fleet_edges()
        self.enemies.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet2 in self.bullets2.sprites():
            bullet2.draw_bullet()

        self.enemies.draw(self.screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()