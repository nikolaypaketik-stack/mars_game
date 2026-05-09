import pygame
from models.move.player_move import PlayerMove
from models.phase.phase import Phase 
import time

class BossMove:
    def __init__(self, player_move):
        self.phase = Phase()  
        self.player = player_move

        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 120, 120)

    def update(self):
        if self.phase.phase == 1:
            if len(self.player.history) > 30:
                self.x, self.y = self.player.history[30]
                self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


