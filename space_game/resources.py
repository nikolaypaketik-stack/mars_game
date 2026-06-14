from functools import lru_cache

import pygame

from space_game.config import asset_file


@lru_cache(maxsize=128)
def load_image(relative_path: str, *, alpha: bool = True) -> pygame.Surface:
    image = pygame.image.load(asset_file(relative_path))
    return image.convert_alpha() if alpha else image.convert()


@lru_cache(maxsize=128)
def load_scaled_image(relative_path: str, size: tuple[int, int]) -> pygame.Surface:
    return pygame.transform.scale(load_image(relative_path), size)
