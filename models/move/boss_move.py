import pygame
from models.move.player_move import PlayerMove
from models.phase.phase import Phase 
import time
import pygame

class BossMove:
    def __init__(self, player_move, screen):
        self.player = player_move
        self.screen = screen
        self.active = False
        self.rect = pygame.Rect(0, 0, 120, 120)
        self.target = pygame.Vector2(0, 0)

    def spawn(self):
        self.active = True
        r = self.screen.get_rect()

        self.rect.centerx = r.centerx + 120
        self.rect.top = r.bottom + 150

        self.target.x = r.centerx + 120
        self.target.y = r.centery - 100

        print(f"Boss spawn: rect={self.rect.topleft}, target={self.target}")

    def update(self):
        if not self.active:
            return

        pos = pygame.Vector2(self.rect.topleft)
        direction = self.target - pos

        pos += direction * 0.05
        self.rect.topleft = (pos.x, pos.y)

        print(f"Boss update: rect={self.rect.topleft}, target={self.target}")