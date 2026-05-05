import pygame

class Player:
    def __init__(self):
        self.speed = 5
        self.hp = 100
        self.oxygen = 100
        self.food = 100
        self.water = 100
        self.x = 100
        self.y = 100  

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed


