import pygame

from space_game.config import asset_path
from space_game.states import GameState


def mixer_ready() -> bool:
    return pygame.mixer.get_init() is not None


class AudioManager:
    def __init__(self) -> None:
        self.music_volume = 0.5
        self.voice_volume = 1.0
        self.music_muted = False

    def apply_music_volume(self) -> None:
        if not mixer_ready():
            return

        pygame.mixer.music.set_volume(0 if self.music_muted else self.music_volume)

    def set_music_volume(self, value: float) -> None:
        self.music_volume = max(0.0, min(1.0, value))
        self.apply_music_volume()

    def toggle_music_mute(self) -> None:
        self.music_muted = not self.music_muted
        self.apply_music_volume()

    def set_voice_volume(self, sound: pygame.mixer.Sound, value: float) -> None:
        self.voice_volume = max(0.0, min(1.0, value))
        sound.set_volume(self.voice_volume)


class SoundtrackManager:
    TRACKS = {
        GameState.INTRO: ("music", "sound_effect", "klava.mp3"),
        GameState.MENU: ("music", "background_music", "menu.mp3"),
        GameState.ACT_ONE: ("music", "background_music", "menu.mp3"),
        GameState.ENDING: ("music", "background_music", "menu.mp3"),
    }

    def __init__(self) -> None:
        self.current_track: str | None = None

    def update(self, game_state: GameState) -> None:
        track_parts = self.TRACKS.get(game_state)
        if track_parts is None:
            return

        self.switch_track(asset_path(*track_parts))

    def switch_track(self, track: str) -> None:
        if not mixer_ready() or self.current_track == track:
            return

        try:
            pygame.mixer.music.load(track)
            pygame.mixer.music.play(-1)
            self.current_track = track
        except pygame.error as exc:
            print(f"Could not play track {track}: {exc}")
