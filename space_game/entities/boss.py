import pygame

from space_game.resources import load_scaled_image


class Boss:
    def __init__(self) -> None:
        self.active = False
        self.rect = pygame.Rect(0, 0, 120, 120)
        self.position = pygame.Vector2(self.rect.center)
        self.target = pygame.Vector2(0, 0)

        self.image_full = load_scaled_image("images/ship/police_ship1.2.png", (120, 120))
        self.image_half = load_scaled_image("images/ship/police_ship1.1.png", (120, 120))
        self.image_low = load_scaled_image("images/ship/police_ship1.0.png", (120, 120))
        self.current_image = self.image_full

    def spawn(self, screen_rect: pygame.Rect) -> None:
        self.active = True
        self.rect.centerx = screen_rect.centerx
        self.rect.top = screen_rect.bottom + 150
        self.position.update(self.rect.center)
        self.target.update(screen_rect.centerx + 150, screen_rect.centery - 100)

    def update(self) -> None:
        if not self.active:
            return

        self.position += (self.target - self.position) * 0.03
        self._sync_rect()

    def chase(self, target_center: tuple[int, int]) -> None:
        if not self.active:
            return

        self.position += (pygame.Vector2(target_center) - self.position) * 0.03
        self._sync_rect()

    def reached_target(self, tolerance: int = 12) -> bool:
        return self.active and self.position.distance_to(self.target) <= tolerance

    def draw(self, surface: pygame.Surface) -> None:
        if self.active:
            surface.blit(self.current_image, self.rect)

    def _sync_rect(self) -> None:
        self.rect.center = (round(self.position.x), round(self.position.y))
