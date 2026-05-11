import pygame

class BossMove:
    def __init__(self, player_move, screen):
        self.player = player_move
        self.screen = screen

        self.active = False

        self.rect = pygame.Rect(0, 0, 120, 120)

        self.target_x = 0
        self.target_y = 0

    def spawn(self):
        self.active = True

        r = self.screen.get_rect()

        self.rect.centerx = r.centerx
        self.rect.top = r.bottom + 150

        self.target_x = r.centerx + 150
        self.target_y = r.centery - 100

    def update(self):
        if not self.active:
            return

        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery

        self.rect.centerx += dx * 0.03
        self.rect.centery += dy * 0.03