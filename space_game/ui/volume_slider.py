import pygame

from space_game.audio.manager import AudioManager


class VolumeSlider:
    def __init__(self, audio: AudioManager, x: int = 50, y: int = 650, width: int = 200) -> None:
        self.audio = audio
        self.volume = audio.music_volume
        self.start_x = x
        self.width = width
        self.track = pygame.Rect(x, y, width, 10)
        self.knob = pygame.Rect(x, y - 5, 10, 20)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type not in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            return
        if not pygame.mouse.get_pressed()[0]:
            return
        if not self.track.collidepoint(event.pos) and not self.knob.collidepoint(event.pos):
            return

        self.volume = (event.pos[0] - self.start_x) / self.width
        self.volume = max(0.0, min(1.0, self.volume))
        self.audio.set_music_volume(self.volume)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (80, 80, 80), self.track, border_radius=4)
        filled = self.track.copy()
        filled.width = int(self.width * self.volume)
        pygame.draw.rect(surface, (70, 170, 105), filled, border_radius=4)

        self.knob.centerx = self.start_x + int(self.volume * self.width)
        pygame.draw.rect(surface, (220, 220, 220), self.knob, border_radius=4)
