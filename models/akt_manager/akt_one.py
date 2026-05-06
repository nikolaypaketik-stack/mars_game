import pygame
from models.background.spase_background import SpaceBackground


class Akt_one:
    def __init__(self):
        self.bg = SpaceBackground()

    def update(self):
        self.bg.update()

    def draw(self, screen):
        self.bg.draw(screen)