import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.bullets = []  # List to store bullet rectangles

        # Create two bullet rectangles at different positions
        bullet1 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        bullet1.topright = ai_game.ship.rect.topright
        self.bullets.append(bullet1)

        bullet2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        bullet2.topleft = ai_game.ship.rect.topleft
        self.bullets.append(bullet2)

        self.y = [float(bullet.y) for bullet in self.bullets]

    def update(self):
        for i in range(len(self.bullets)):
            self.y[i] -= self.settings.bullet_speed
            self.bullets[i].y = self.y[i]

    def draw_bullet(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.color, bullet)


class Bullet(Sprite):
    
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.charged_shot = False
        
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)