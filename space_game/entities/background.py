import random

import pygame

from space_game.config import SCREEN_HEIGHT
from space_game.resources import load_image


class SpaceBackground:
    def __init__(self) -> None:
        self.images = [
            load_image("images/spase_background/kosmo.bg2.png"),
            load_image("images/spase_background/kosmo.bg3.png"),
            load_image("images/spase_background/kosmo.bg5.png"),
            load_image("images/spase_background/kosmo.bg6.png"),
        ]
        self.rare_image = load_image("images/spase_background/kosmo.bg4.png")

        self.current_image = self.images[0]
        self.next_image = self.images[1]
        self.y1 = 0.0
        self.y2 = -float(SCREEN_HEIGHT)
        self.speed = 0.2

    def update(self) -> None:
        self.y1 += self.speed
        self.y2 += self.speed

        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = -float(SCREEN_HEIGHT)
            self.current_image = self._next_image()

        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = -float(SCREEN_HEIGHT)
            self.next_image = self._next_image()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.current_image, (0, int(self.y1)))
        surface.blit(self.next_image, (0, int(self.y2)))

    def _next_image(self) -> pygame.Surface:
        if random.randint(1, 10) == 1:
            return self.rare_image
        return random.choice(self.images)
