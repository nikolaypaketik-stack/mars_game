import pygame
import random
from models.complications_for_the_player.meteor import Meteor

class MeteorManager():
    def __init__(self, speed_min, speed_max):
        self.meteors = []
        self.phase = 1
        self.image = random.choice(self.images)
        self.x = random.randint(1300, 1600)
        self.y = random.randint(-100, 720)


    def spawn(self, speed_min, speed_max):
        if self.phase == 1:   
            self.speed_x = random.randint(speed_min, speed_max)
            self.speed_y = random.randint(1, 5)
            self.x = random.randint(1300, 1600)
            self.y = random.randint(-100, 720)     
               


    def update(self):
        ...

    def draw(self):
        ...