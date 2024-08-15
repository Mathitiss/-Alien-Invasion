import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect1 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect1.topright = ai_game.ship.rect.topright

        self.rect2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2.topleft = ai_game.ship.rect.topleft

        self.y = float(self.rect1.y)
        self.y = float(self.rect2.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect1.y = self.y
        self.rect2.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)