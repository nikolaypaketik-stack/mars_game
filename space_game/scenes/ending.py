import pygame

from space_game.config import ENDING_DURATION_MS, ENDING_TEXT
from space_game.scenes.base import Scene


class EndingScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.started_at = pygame.time.get_ticks()
        self.font = pygame.font.SysFont("arial", 40)

    def update(self, delta_ms: int) -> None:
        if pygame.time.get_ticks() - self.started_at >= ENDING_DURATION_MS:
            self.quit_requested = True

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 0))
        text = self.font.render(ENDING_TEXT, True, (255, 255, 255))
        surface.blit(text, text.get_rect(center=surface.get_rect().center))
