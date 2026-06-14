import pygame

from space_game.audio.manager import AudioManager, SoundtrackManager
from space_game.config import FPS, SCREEN_SIZE
from space_game.scenes.act_one import ActOneScene
from space_game.scenes.ending import EndingScene
from space_game.scenes.intro import IntroScene
from space_game.scenes.menu import MenuScene
from space_game.scenes.base import Scene
from space_game.states import GameState
from space_game.ui.volume_slider import VolumeSlider


class Game:
    def __init__(self) -> None:
        pygame.init()
        self._init_mixer()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Space Game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.audio = AudioManager()
        self.soundtrack = SoundtrackManager()
        self.volume_slider = VolumeSlider(self.audio)

        self.state = GameState.INTRO
        self.scene = self._create_scene(self.state)
        self.soundtrack.update(self.state)

    def run(self) -> None:
        try:
            while self.running:
                delta_ms = self.clock.tick(FPS)
                self._handle_events()
                self._consume_scene_requests()

                if not self.running:
                    break

                self.scene.update(delta_ms)
                self._consume_scene_requests()

                self.soundtrack.update(self.state)
                self._draw()
        finally:
            pygame.quit()

    def _init_mixer(self) -> None:
        try:
            pygame.mixer.init()
        except pygame.error as exc:
            print(f"Audio disabled: {exc}")

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                continue

            self.scene.handle_event(event)
            self.volume_slider.handle_event(event)

    def _consume_scene_requests(self) -> None:
        if self.scene.quit_requested:
            self.running = False
            return

        if self.scene.next_state is not None:
            self._change_state(self.scene.next_state)

    def _change_state(self, state: GameState) -> None:
        self.state = state
        self.scene = self._create_scene(state)
        self.soundtrack.update(state)

    def _create_scene(self, state: GameState) -> Scene:
        screen_rect = self.screen.get_rect()

        if state == GameState.INTRO:
            return IntroScene()
        if state == GameState.MENU:
            return MenuScene(screen_rect)
        if state == GameState.ACT_ONE:
            return ActOneScene(screen_rect)
        if state == GameState.ENDING:
            return EndingScene()

        raise ValueError(f"Unsupported game state: {state}")

    def _draw(self) -> None:
        self.scene.draw(self.screen)

        if self.state in {GameState.MENU, GameState.ACT_ONE}:
            self.volume_slider.draw(self.screen)

        pygame.display.flip()
