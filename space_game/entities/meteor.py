import random

import pygame

from space_game.config import SCREEN_HEIGHT, SCREEN_WIDTH
from space_game.resources import load_image


class Meteor:
    def __init__(self, speed_min: int, speed_max: int, image: pygame.Surface) -> None:
        self.speed_min = speed_min
        self.speed_max = speed_max
        self.image = image
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(0, 0)
        self.speed = pygame.Vector2(0, 0)
        self.reset()

    def reset(self) -> None:
        self.position.update(
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 320),
            random.randint(-100, SCREEN_HEIGHT),
        )
        self.speed.update(
            -random.randint(self.speed_min, self.speed_max),
            random.randint(1, 5),
        )
        self._sync_rect()

    def update(self) -> None:
        self.position += self.speed
        self._sync_rect()

        if self.rect.right < 0 or self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

    def _sync_rect(self) -> None:
        self.rect.topleft = (round(self.position.x), round(self.position.y))


class MeteorManager:
    PHASE_SETTINGS = {
        1: (3, 6, 2),
        2: (8, 14, 6),
    }

    def __init__(self, phase: int = 1) -> None:
        self.phase = phase
        self.images = [
            load_image("images/meteor/meteorit1.png"),
            load_image("images/meteor/meteorit2.png"),
            load_image("images/meteor/meteorit3.png"),
        ]
        self.meteors: list[Meteor] = []

    def spawn(self) -> None:
        settings = self.PHASE_SETTINGS.get(self.phase)
        if settings is None:
            return

        speed_min, speed_max, meteor_count = settings
        self.meteors = [
            Meteor(speed_min, speed_max, random.choice(self.images))
            for _ in range(meteor_count)
        ]

    def update(self) -> None:
        for meteor in self.meteors:
            meteor.update()

    def draw(self, surface: pygame.Surface) -> None:
        for meteor in self.meteors:
            meteor.draw(surface)
