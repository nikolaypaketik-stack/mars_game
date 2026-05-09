import pygame
import random
from models.complications_for_the_player.meteor import Meteor
from models.phase.phase import Phase

class MeteorManager:
    def __init__(self):
        self.meteors = []
        self.phase = 1

        self.images = [
            pygame.image.load("assets/images/meteor/meteorit1.png").convert_alpha(),
            pygame.image.load("assets/images/meteor/meteorit2.png").convert_alpha(),
            pygame.image.load("assets/images/meteor/meteorit3.png").convert_alpha(),
        ]

        print(len(self.meteors))

    def spawn(self):
        print("SPAWN")

        if self.phase == 1:
            speed_min = 3
            speed_max = 6
            meteor_count = 2

        elif self.phase == 2:
            speed_min = 8
            speed_max = 14
            meteor_count = 6

        else:
            return

        for i in range(meteor_count):
            image = random.choice(self.images)
            self.meteors.append(Meteor(speed_min, speed_max, image))

    def update(self):
        for meteor in self.meteors:
            meteor.update()
            

    def draw(self, screen):
        for meteor in self.meteors:
            meteor.draw(screen)