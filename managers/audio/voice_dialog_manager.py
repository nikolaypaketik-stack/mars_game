import pygame


class VoiceDialogue:
    def __init__(self, lines):

        self.lines = lines
        self.index = 0

        self.finished = False

        self.channel = pygame.mixer.Channel(1)

    def start(self):
        self.play_current()

    def play_current(self):

        if self.index >= len(self.lines):
            self.finished = True
            return

        sound = pygame.mixer.Sound(
            self.lines[self.index]
        )

        self.channel.play(sound)

    def update(self):

        if self.finished:
            return


        if not self.channel.get_busy():

            self.index += 1

            self.play_current()