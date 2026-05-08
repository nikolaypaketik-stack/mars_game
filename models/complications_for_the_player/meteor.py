import pygame
import random

class Meteor:

    def __init__(self, speed_min, speed_max):

        print("meteor created")

        try:
            self.images = [
                pygame.image.load("assets/images/meteor/meteorit1.png").convert_alpha(),
                pygame.image.load("assets/images/meteor/meteorit2.png").convert_alpha(),
                pygame.image.load("assets/images/meteor/meteorit3.png").convert_alpha(),
            ]
        except Exception as e:
            print(e)
        self.image = random.choice(self.images)

        self.x = random.randint(1300, 1600)
        self.y = random.randint(-100, 720)

        self.speed_x = random.randint(speed_min, speed_max)
        self.speed_y = random.randint(1, 5)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x -= self.speed_x
        self.y += self.speed_y

        self.rect.x = self.x
        self.rect.y = self.y
    
    def spawn(self):

        if self.phase == 1:
            speed_min = 3
            speed_max = 6
            meteor_count = 2

        elif self.phase == 2:
            speed_min = 8
            speed_max = 14
            meteor_count = 6


        for i in range(meteor_count):
            self.meteors.append(Meteor(speed_min, speed_max))

            print(len(self.meteors))

    def draw(self, screen):

        screen.blit(self.image, (self.x, self.y))