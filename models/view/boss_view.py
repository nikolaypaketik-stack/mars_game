import pygame
from models.phase.phase import Phase


class BossView:
    def __init__(self, screen, boss_move):
        self.screen = screen
        self.boss_move = boss_move

        self.phase = None
        self.img_full = pygame.image.load(
            "assets/images/ship/police_ship1.2.png"
        ).convert_alpha()

        self.img_half = pygame.image.load(
            "assets/images/ship/police_ship1.1.png"
        ).convert_alpha()

        self.img_low = pygame.image.load(
            "assets/images/ship/police_ship1.0.png"
        ).convert_alpha()

        self.img_full = pygame.transform.scale(self.img_full, (120, 120))
        self.img_half = pygame.transform.scale(self.img_half, (120, 120))
        self.img_low = pygame.transform.scale(self.img_low, (120, 120))

        self.current_img = self.img_full

    def update(self):

        phase = 1  

        if phase == 1:
            self.current_img = self.img_full
        elif phase == 2:
            self.current_img = self.img_half
        elif phase == 3:
            self.current_img = self.img_low

    def draw(self):
        self.screen.blit(self.current_img, self.boss_move.rect)