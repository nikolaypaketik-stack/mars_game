import pygame
import random
from models.complications_for_the_player.meteor import Meteor

class MeteorManager:
    def __init__(self):
        self.meteors = []
        self.phase = 1
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
        for i in range(meteor_count):
            self.meteors.append(Meteor(speed_min, speed_max))


    def update(self):
        for meteor in self.meteors:
            meteor.update()


    def draw(self, screen):
        for meteor in self.meteors:
            meteor.draw(screen)