import pygame
from models.background.spase_background import SpaceBackground
from models.move.player_move import PlayerMove

class Akt_one:

    def __init__(self):
        self.bg = SpaceBackground()
        self.player = PlayerMove()

    def handle_event(self, event):
        pass

    def update(self):
        self.bg.update()
        self.player.update()

    def draw(self, screen):
        self.bg.draw(screen)
        self.player.draw(screen)