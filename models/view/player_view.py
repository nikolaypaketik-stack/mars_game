import pygame 
from models.move.player_move import PlayerMove


class PlayerView:
    def __init__(self, screen, player_move):
        self.screen = screen
        self.player_move = player_move
        self.phase = 1


        self.img_normal = pygame.image.load(
            "assets/images/ship/spaseship1.1.png"
        ).convert_alpha()

        self.img_thrust = pygame.image.load(
            "assets/images/ship/spaseship2.png"
        ).convert_alpha()

        self.img_normal = pygame.transform.scale(self.img_normal, (120, 120))
        self.img_thrust = pygame.transform.scale(self.img_thrust, (120, 120))

        self.angle = 0
        self.thrust = False
        

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if self.phase == 1:
            self.thrust = keys[pygame.K_w]

            if keys[pygame.K_a]:
                self.angle = 90
            elif keys[pygame.K_d]:
                self.angle = -90
            elif keys[pygame.K_w]:
                self.angle = 0
            elif keys[pygame.K_s]:
                self.angle = 0
            

    def update(self):
        self.handle_input()

        img = self.img_thrust if self.thrust else self.img_normal

        self.rotated_img = pygame.transform.rotate(img, self.angle)

        self.rect = self.rotated_img.get_rect(center=self.player_move.rect.center)
    
    def draw(self):
        self.screen.blit(self.rotated_img, self.rect)
