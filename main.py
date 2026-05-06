import pygame
from models.audio.sound_manager import SoundManager
from models.audio.settings import Settings
from models.audio.audio_manager import AudioManager
from models.background.spase_background import SpaceBackground
from models.akt_manager.menu import Menu

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
game_state = "menu"

running = True
while running:
    for event in pygame.event.get():
        scene.new_akt_event(event)

    pygame.display.update()

pygame.quit()
