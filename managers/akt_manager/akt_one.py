import pygame
import time

from models.background.spase_background import SpaceBackground
from models.move.player_move import PlayerMove
from managers.complications_for_the_player.meteor_manager import MeteorManager
from models.view.player_view import PlayerView

from models.move.boss_move import BossMove
from models.view.boss_view import BossView


class Akt_one:

    def __init__(self, screen, dialog):

        self.screen = screen

        self.start_time = time.time()

        self.boss_spawned = False

        self.dialog = dialog
        self.dialog_started = False
        self.dialog_active = False

        self.start_chase = False

        self.bg = SpaceBackground()

        self.player_move = PlayerMove(screen)
        self.player_view = PlayerView(screen, self.player_move)

        self.meteor_manager = MeteorManager()
        self.meteor_manager.spawn()

        self.boss_move = BossMove(self.player_move, screen)
        self.boss_view = BossView(screen, self.boss_move)

        self.show_text = False
        self.text_start = 0

    def handle_event(self, event):
        pass

    def update(self):

        self.bg.update()



        if self.dialog_active:
            self.player_move.update(True)
        else:
            self.player_move.update(False)

        self.player_view.update()

  

        self.meteor_manager.update()



        if not self.boss_spawned:

            if time.time() - self.start_time > 15:

                self.boss_move.spawn()

                self.boss_spawned = True


        self.boss_move.update()
        self.boss_view.update()



        if self.boss_spawned and not self.dialog_started:

            self.player_move.move_to_center(self.screen)


            if self.boss_move.rect.y <= self.boss_move.target_y + 10:

                self.dialog.start()

                self.dialog_started = True
                self.dialog_active = True



        if self.dialog_started:

            self.dialog.update()


            if self.dialog.finished:

                self.dialog_active = False
                self.start_chase = True



        if self.start_chase:


            if len(self.player_move.history) > 120:

                x, y = self.player_move.history[-120]

                self.boss_move.rect.x += (
                    x - self.boss_move.rect.x
                ) * 0.03

                self.boss_move.rect.y += (
                    y - self.boss_move.rect.y
                ) * 0.03

    def draw(self, screen):

        self.bg.draw(screen)

        self.meteor_manager.draw(screen)

        self.boss_view.draw()

        self.player_view.draw()