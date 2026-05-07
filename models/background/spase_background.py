import pygame
import random

class SpaceBackground:
    def __init__(self):
        self.images = [
            pygame.image.load("assets/images/spase_background/kosmo.bg2.png"),
            pygame.image.load("assets/images/spase_background/kosmo.bg3.png"),
            pygame.image.load("assets/images/spase_background/kosmo.bg5.png"),
            pygame.image.load("assets/images/spase_background/kosmo.bg6.png")
        ]

        self.rare_image = pygame.image.load("assets/images/spase_background/kosmo.bg4.png")

        self.current_img = self.images[0]
        self.next_img = self.images[1]

        self.y1 = 0
        self.y2 = -720

        self.speed = 0.2


    def update(self):
        self.y1 += self.speed
        self.y2 += self.speed

        if self.y1 >= 720:
            self.y1 = -720
            self.current_img = self.get_next_image()

        if self.y2 >= 720:
            self.y2 = -720
            self.next_img = self.get_next_image()


    def get_next_image(self):
        if random.randint(1, 10) == 1:
            return self.rare_image

        return random.choice(self.images)


    def draw(self, screen):
        screen.blit(self.current_img, (0, self.y1))
        screen.blit(self.next_img, (0, self.y2))
