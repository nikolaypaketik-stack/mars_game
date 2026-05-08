import pygame
from models.audio.sound_manager import SoundManager
from models.audio.settings import Settings
from models.audio.audio_manager import AudioManager
from models.background.spase_background import SpaceBackground
from models.akt_manager.menu import Menu
from models.akt_manager.akt_one import Akt_one

pygame.init()
pygame.mixer.init()

audio = AudioManager()
settings = Settings(audio)

screen = pygame.display.set_mode((1280, 720))


pygame.init()
pygame.mixer.init()

audio = AudioManager()
settings = Settings(audio)

sound = SoundManager()

menu = Menu()
act1 = Akt_one(screen)

current_scene = act1
game_state = "akt1"

running = True

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        result = current_scene.handle_event(event)

        if result == "akt1":
            current_scene = act1
            game_state = "akt1"

        elif result == "exit":
            running = False

        settings.handle_event(event)

    current_scene.update()

    in_bass_zone = getattr(current_scene, "in_bass_zone", False)

    sound.update(game_state, in_bass_zone)

    screen.fill((0, 0, 0))

    current_scene.draw(screen)

    settings.draw(screen)

    pygame.display.flip()

