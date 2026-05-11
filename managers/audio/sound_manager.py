import pygame


class SoundManager:
    def __init__(self):
        self.current_track = None
        self.current_state = None

    def switch_track(self, track):
        if self.current_track == track:
            return

        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)

        self.current_track = track

    def update(self, game_state):


        if game_state == "intro":
            self.switch_track(
                "assets/music/sound_effect/klava.mp3"
            )


        elif game_state == "menu":
            self.switch_track(
                "assets/music/background_music/menu.mp3"
            )


        elif game_state == "akt1":
            self.switch_track(
                "assets/music/background_music/menu.mp3"
            )