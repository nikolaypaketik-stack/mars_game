import pygame
from models.background.spase_background import SpaceBackground
from models.move.player_move import PlayerMove
from managers.complications_for_the_player.meteor_manager import MeteorManager
from models.view.player_view import PlayerView
from models.phase.phase import Phase
from models.move.boss_move import BossMove
from models.view.boss_view import BossView
import time

class Akt_one:
    
    def __init__(self, screen):
        self.screen = screen
        self.start_time = time.time()
        self.boss_spawned = False

        self.bg = SpaceBackground()

        self.player_move = PlayerMove(screen)
        self.player_view = PlayerView(screen, self.player_move)

        self.meteor_manager = MeteorManager()
        self.meteor_manager.spawn()

        self.boss_move = BossMove(self.player_move, screen)
        self.boss_view = BossView(screen, self.boss_move)

    def handle_event(self, event):
        pass

    def update(self):
        self.bg.update()
        self.player_move.update(self.boss_spawned)
        self.player_view.update()
        self.meteor_manager.update()

        if not self.boss_spawned:
            if time.time() - self.start_time > 15:
                print("Boss spawning...")
                self.boss_move.spawn()
                self.boss_spawned = True

        if self.boss_spawned:
            self.player_move.move_to_center(self.screen)

        self.boss_move.update()
        self.boss_view.update()

        # Отладка позиции игрока
        print(f"Player position: {self.player_move.rect.topleft}")

    def draw(self, screen):
        self.bg.draw(screen)
        self.meteor_manager.draw(screen)
        self.boss_view.draw()
        self.player_view.draw()