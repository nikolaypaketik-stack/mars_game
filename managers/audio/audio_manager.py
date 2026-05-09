import pygame

class AudioManager:
    def __init__(self):
        self.music_volume = 0.5
        self.voice_volume = 1.0

        self.music_muted = False

    # 🔊 музыка
    def set_music_volume(self, value):
        self.music_volume = value

        if not self.music_muted:
            pygame.mixer.music.set_volume(self.music_volume)

    # 🔇 mute только музыки
    def toggle_music_mute(self):
        self.music_muted = not self.music_muted

        if self.music_muted:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(self.music_volume)

    # 🎤 эффекты / голос (пока заготовка)
    def set_voice_volume(self, sound, value):
        self.voice_volume = value
        sound.set_volume(self.voice_volume)