import pygame

from space_game.config import INTRO_DURATION_MS, INTRO_TEXT, INTRO_TYPE_SPEED_MS
from space_game.scenes.base import Scene
from space_game.states import GameState


class IntroScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.started_at = pygame.time.get_ticks()
        self.last_text_update = self.started_at
        self.visible_characters = 0
        self.font = pygame.font.SysFont("arial", 48)

    def update(self, delta_ms: int) -> None:
        now = pygame.time.get_ticks()

        if self.visible_characters < len(INTRO_TEXT):
            if now - self.last_text_update >= INTRO_TYPE_SPEED_MS:
                self.visible_characters += 1
                self.last_text_update = now

        if now - self.started_at >= INTRO_DURATION_MS:
            self.next_state = GameState.MENU

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 0))
        shown_text = INTRO_TEXT[: self.visible_characters]
        text = self.font.render(shown_text, True, (255, 255, 255))
        surface.blit(text, text.get_rect(center=surface.get_rect().center))
