import pygame
import models.audio.sound_track
class SoundManager:
    def __init__(self):
        self.current_track = None
        self.current_time = 0
        self.in_bass_zone = False
        self.current_state = None


    def switch_track(self, new_track):
        if self.current_track == new_track:
            return
        
        pos = pygame.mixer.music.get_pos()
        if pos > 0:
            self.current_time = pos / 1000
        else:
            self.current_time = 0

        pygame.mixer.music.load(new_track)
        pygame.mixer.music.play(-1, start=self.current_time)
        self.current_track = new_track
    
    def update(self, game_state, in_bass_zone):
        if game_state != self.current_state:

            if game_state == "menu":
                self.switch_track("assets/music/background_music/menu.mp3")


            if game_state == "akt1":
                self.switch_track("game.mp3")

            self.current_state = game_state

        if game_state == "menu":

            if in_bass_zone:
                self.switch_track("assets/music/instruments/bass.mp3")
            else:
                self.switch_track("assets/music/background_music/menu.mp3")

            self.in_bass_zone = in_bass_zone

    