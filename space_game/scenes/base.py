from __future__ import annotations

import pygame

from space_game.states import GameState


class Scene:
    def __init__(self) -> None:
        self.next_state: GameState | None = None
        self.quit_requested = False

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta_ms: int) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        pass
