import pygame

class AudioManager:
    def __init__(self):
        self.music_volume = 0.5
        self.voice_volume = 1.2
        self.music_muted = False

    def apply_music_volume(self):
        volume = 0 if self.music_muted else self.music_volume
        pygame.mixer.music.set_volume(volume)

    def set_music_volume(self, value):
        self.music_volume = value
        self.apply_music_volume()

    def toggle_music_mute(self):
        self.music_muted = not self.music_muted
        self.apply_music_volume()

    def set_voice_volume(self, sound, value):
        self.voice_volume = value
        sound.set_volume(self.voice_volume)