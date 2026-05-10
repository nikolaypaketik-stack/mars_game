import pygame
from managers.audio.sound_manager import SoundManager
from models.audio.settings import AudioSettings
from managers.audio.audio_manager import AudioManager
from managers.akt_manager.akt_one import Akt_one
from managers.akt_manager.menu_org import MenuOrg

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

audio = AudioManager()
settings = AudioSettings(audio)
sound = SoundManager()

menu_org = MenuOrg()
menu_org.run()   

act1 = Akt_one(screen)

current_scene = None
game_state = "menu"

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        settings.handle_event(event)

    if menu_org.game_state == "akt1":
        if current_scene is None:
            current_scene = act1
            game_state = "akt1"

    if current_scene:
        current_scene.update()

    sound.update(game_state, getattr(current_scene, "in_bass_zone", False))

    screen.fill((0, 0, 0))

    if current_scene:
        current_scene.draw(screen)

    settings.draw(screen)

    pygame.display.flip()

pygame.quit()