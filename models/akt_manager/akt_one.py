import pygame
from models.background.spase_background import SpaceBackground
from models.move.player_move import PlayerMove
from models.complications_for_the_player.meteor_manager import MeteorManager
from models.view.player_view import PlayerView


class Akt_one:

    def __init__(self, screen):
        self.screen = screen

        self.bg = SpaceBackground()

        self.player_move = PlayerMove(screen)
        self.player_view = PlayerView(screen, self.player_move)

        self.meteor_manager = MeteorManager()
        self.meteor_manager.spawn()

    def handle_event(self, event):
        pass

    def update(self):
        self.bg.update()
        self.player_move.update()
        self.player_view.update()
        self.meteor_manager.update()

    def draw(self, screen):
        self.bg.draw(screen)
        self.meteor_manager.draw(screen)

        self.player_view.draw()