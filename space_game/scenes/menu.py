import pygame

from space_game.resources import load_image
from space_game.scenes.base import Scene
from space_game.states import GameState


class MenuScene(Scene):
    def __init__(self, screen_rect: pygame.Rect) -> None:
        super().__init__()
        self.screen_rect = screen_rect
        self.background = load_image("images/menu/menu1.png")
        self.background_rect = self.background.get_rect(center=screen_rect.center)
        self.title_font = pygame.font.SysFont("arial", 58, bold=True)
        self.button_font = pygame.font.SysFont("arial", 32, bold=True)
        self.buttons = {
            "start": pygame.Rect(0, 0, 240, 64),
            "exit": pygame.Rect(0, 0, 240, 64),
        }
        self.buttons["start"].center = (screen_rect.centerx, screen_rect.centery - 50)
        self.buttons["exit"].center = (screen_rect.centerx, screen_rect.centery + 40)
        self.hovered: str | None = None

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.buttons["start"].collidepoint(event.pos):
                self.next_state = GameState.ACT_ONE
            elif self.buttons["exit"].collidepoint(event.pos):
                self.quit_requested = True

    def update(self, delta_ms: int) -> None:
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = None

        for name, rect in self.buttons.items():
            if rect.collidepoint(mouse_pos):
                self.hovered = name
                break

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 0))
        surface.blit(self.background, self.background_rect)

        title = self.title_font.render("SPACE GAME", True, (240, 240, 240))
        surface.blit(title, title.get_rect(center=(self.screen_rect.centerx, 120)))

        self._draw_button(surface, self.buttons["start"], "START", self.hovered == "start")
        self._draw_button(surface, self.buttons["exit"], "EXIT", self.hovered == "exit")

    def _draw_button(
        self,
        surface: pygame.Surface,
        rect: pygame.Rect,
        text: str,
        hovered: bool,
    ) -> None:
        fill = (36, 92, 63) if hovered else (30, 30, 34)
        outline = (230, 230, 230) if hovered else (120, 120, 130)
        pygame.draw.rect(surface, fill, rect, border_radius=8)
        pygame.draw.rect(surface, outline, rect, width=2, border_radius=8)

        label = self.button_font.render(text, True, (255, 255, 255))
        surface.blit(label, label.get_rect(center=rect.center))
