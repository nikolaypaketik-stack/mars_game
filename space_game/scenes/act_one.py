import pygame

from space_game.audio.dialogue import VoiceDialogue
from space_game.config import BOSS_SPAWN_DELAY_MS, CHASE_HISTORY_DELAY
from space_game.data.dialogues import COP_DIALOG
from space_game.entities.background import SpaceBackground
from space_game.entities.boss import Boss
from space_game.entities.meteor import MeteorManager
from space_game.entities.player import Player
from space_game.scenes.base import Scene
from space_game.states import GameState


class ActOneScene(Scene):
    def __init__(self, screen_rect: pygame.Rect) -> None:
        super().__init__()
        self.screen_rect = screen_rect
        self.started_at = pygame.time.get_ticks()

        self.background = SpaceBackground()
        self.player = Player(screen_rect)
        self.boss = Boss()
        self.meteors = MeteorManager()
        self.meteors.spawn()
        self.dialogue = VoiceDialogue(COP_DIALOG)

        self.boss_spawned = False
        self.dialogue_started = False
        self.dialogue_active = False
        self.start_chase = False

    def update(self, delta_ms: int) -> None:
        now = pygame.time.get_ticks()

        if not self.boss_spawned and now - self.started_at >= BOSS_SPAWN_DELAY_MS:
            self.boss.spawn(self.screen_rect)
            self.boss_spawned = True

        force_center = self.dialogue_active or (self.boss_spawned and not self.dialogue_started)

        self.background.update()
        self.player.update(self.screen_rect, force_center=force_center)
        self.meteors.update()
        self.boss.update()

        if self.boss_spawned and not self.dialogue_started and self.boss.reached_target():
            self.dialogue.start()
            self.dialogue_started = True
            self.dialogue_active = True

        if self.dialogue_started:
            self.dialogue.update()

            if self.dialogue.finished:
                self.dialogue_active = False
                self.start_chase = True
                self.next_state = GameState.ENDING

        if self.start_chase and len(self.player.history) > CHASE_HISTORY_DELAY:
            self.boss.chase(self.player.history[-CHASE_HISTORY_DELAY])

    def draw(self, surface: pygame.Surface) -> None:
        self.background.draw(surface)
        self.meteors.draw(surface)
        self.boss.draw(surface)
        self.player.draw(surface)
