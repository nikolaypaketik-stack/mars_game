import pygame

class VoiceDialogue:
    def __init__(self, lines):
        self.lines = lines
        self.index = 0
        self.finished = False
        self.playing = False

    def start(self):
        self.index = 0
        self.finished = False
        self.play_current()

    def play_current(self):
        if self.index >= len(self.lines):
            self.finished = True
            return

        pygame.mixer.music.load(self.lines[self.index])
        pygame.mixer.music.play()

        self.playing = True

    def update(self):
        if self.finished:
            return

        # если текущий звук закончился → следующий
        if not pygame.mixer.music.get_busy():
            self.index += 1
            self.play_current()