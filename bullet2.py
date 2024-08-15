import pygame
from pygame.sprite import Sprite

class Bullet2(Sprite):
    def __init__(self, ai_game2):
        super().__init__()
        self.screen = ai_game2.screen
        self.settings = ai_game2.settings
        self.color = self.settings.bullet2_color

        self.rect3 = pygame.Rect(0, 0, self.settings.bullet2_width, self.settings.bullet2_height)
        self.rect3.center = ai_game2.ship.rect.center

        self.rect4 = pygame.Rect(0, 0, self.settings.bullet2_width, self.settings.bullet2_height)
        self.rect4.center = ai_game2.ship.rect.center

        self.x1 = float(self.rect3.x)
        self.x2 = float(self.rect4.x)

    def update(self):
        self.x1 += self.settings.bullet2_speed
        self.x2 -= self.settings.bullet2_speed
        self.rect3.x = self.x1
        self.rect4.x = self.x2

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect3)
        pygame.draw.rect(self.screen, self.color, self.rect4)