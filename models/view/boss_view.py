import pygame 
from models.move.boss_move import BossMove
from models.phase.phase import Phase 

class BossView:
    def __init__(self, screen, boss_move):
        self.screen = screen
        self.boss_move = boss_move
        self.phase = Phase


        self.img_with_full_drone = pygame.image.load(
            "assets/images/ship/police_ship1.2.png"
        ).convert_alpha()

        self.img_with_half_drone = pygame.image.load(
            "assets/images/ship/police_ship1.1.png"
        ).convert_alpha()

        self.img_without_drone = pygame.image.load(
            "assets/images/ship/police_ship1.0.png"
        ).convert_alpha()

        self.img_with_full_drone = pygame.transform.scale(self.img_with_full_drone, (120, 120))
        self.img_with_half_drone = pygame.transform.scale(self.img_with_half_drone, (120, 120))
        self.img_without_drone = pygame.transform.scale(self.img_without_drone, (120, 120))

        self.current_img = self.img_with_full_drone



        self.angle = 0
        self.thrust = False
    
    def update(self):
        if self.phase == 1:
            self.current_img = self.img_with_full_drone
        if self.phase == 2:
            self.current_img = self.img_with_half_drone
        if self.phase== 3:
            self.current_img = self.img_without_drone
    

    def draw(self):
        self.screen.blit(self.current_img, (500, 200)) 