import pygame

from space_game.audio.manager import mixer_ready
from space_game.config import asset_file


class VoiceDialogue:
    def __init__(self, lines: tuple[str, ...], channel_id: int = 1) -> None:
        self.lines = lines
        self.channel = pygame.mixer.Channel(channel_id) if mixer_ready() else None
        self.index = 0
        self.finished = False

    def start(self) -> None:
        self.index = 0
        self.finished = False
        self._play_current()

    def stop(self) -> None:
        if self.channel is not None:
            self.channel.stop()
        self.finished = True

    def update(self) -> None:
        if self.finished or self.channel is None:
            return

        if not self.channel.get_busy():
            self.index += 1
            self._play_current()

    def _play_current(self) -> None:
        if self.index >= len(self.lines):
            self.finished = True
            return

        if self.channel is None:
            self.finished = True
            return

        try:
            sound = pygame.mixer.Sound(asset_file(self.lines[self.index]))
            self.channel.play(sound)
        except pygame.error as exc:
            print(f"Could not play voice line {self.lines[self.index]}: {exc}")
            self.index += 1
            self._play_current()
