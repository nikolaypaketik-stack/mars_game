from collections import deque

import pygame

from space_game.resources import load_scaled_image


class Player:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.speed = 2.0
        self.body_rect = pygame.Rect(0, 0, 50, 50)
        self.body_rect.center = screen_rect.center
        self.position = pygame.Vector2(self.body_rect.center)
        self.history: deque[tuple[int, int]] = deque(maxlen=900)

        self.image_normal = load_scaled_image("images/ship/spaseship1.1.png", (120, 120))
        self.image_thrust = load_scaled_image("images/ship/spaseship2.png", (120, 120))
        self.current_image = self.image_normal
        self.image_rect = self.current_image.get_rect(center=self.body_rect.center)

        self.angle = 0
        self.thrust = False

    def update(self, screen_rect: pygame.Rect, *, force_center: bool = False) -> None:
        keys = pygame.key.get_pressed()

        if force_center:
            self.move_towards(screen_rect.center)
        else:
            self._handle_keyboard(keys)

        self._sync_rect()
        self.body_rect.clamp_ip(screen_rect)
        self.position.update(self.body_rect.center)
        self.history.append(self.body_rect.center)
        self._update_sprite(keys, force_center=force_center)

    def move_towards(self, target: tuple[int, int], factor: float = 0.03) -> None:
        self.position += (pygame.Vector2(target) - self.position) * factor

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.current_image, self.image_rect)

    def _handle_keyboard(self, keys: pygame.key.ScancodeWrapper) -> None:
        movement = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            movement.y -= self.speed
        if keys[pygame.K_s]:
            movement.y += self.speed
        if keys[pygame.K_a]:
            movement.x -= self.speed
        if keys[pygame.K_d]:
            movement.x += self.speed

        self.position += movement

    def _update_sprite(self, keys: pygame.key.ScancodeWrapper, *, force_center: bool) -> None:
        self.thrust = bool(keys[pygame.K_w] and not force_center)

        if not force_center:
            if keys[pygame.K_a]:
                self.angle = 90
            elif keys[pygame.K_d]:
                self.angle = -90
            elif keys[pygame.K_w] or keys[pygame.K_s]:
                self.angle = 0

        image = self.image_thrust if self.thrust else self.image_normal
        self.current_image = pygame.transform.rotate(image, self.angle)
        self.image_rect = self.current_image.get_rect(center=self.body_rect.center)

    def _sync_rect(self) -> None:
        self.body_rect.center = (round(self.position.x), round(self.position.y))
