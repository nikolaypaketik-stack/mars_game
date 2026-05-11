import pygame

from managers.audio.sound_manager import SoundManager
from models.audio.settings import AudioSettings
from managers.audio.audio_manager import AudioManager

from managers.akt_manager.akt_one import Akt_one
from managers.akt_manager.menu_org import MenuOrg

from managers.audio.voice_dialog_manager import VoiceDialogue
from models.audio.dialog.cops_scene import COP_DIALOG


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

audio = AudioManager()
settings = AudioSettings(audio)
sound = SoundManager()

game_state = "intro"
intro_start = pygame.time.get_ticks()

intro_text = "десь на околицях марса"
intro_index = 0
intro_last_update = pygame.time.get_ticks()
intro_speed = 80

menu_org = MenuOrg()

dialog = VoiceDialogue(COP_DIALOG)
act1 = Akt_one(screen, dialog)

current_scene = None
running = True


end_game = False
close_time = None


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        settings.handle_event(event)


    if game_state == "intro":
        screen.fill((0, 0, 0))

        font = pygame.font.SysFont("arial", 48)
        now = pygame.time.get_ticks()

        if intro_index < len(intro_text):
            if now - intro_last_update > intro_speed:
                intro_index += 1
                intro_last_update = now

        shown_text = intro_text[:intro_index]

        text = font.render(shown_text, True, (255, 255, 255))
        rect = text.get_rect(center=screen.get_rect().center)
        screen.blit(text, rect)

        sound.update(game_state)

        if pygame.time.get_ticks() - intro_start > 5000:
            game_state = "menu"
            menu_org.run()

        pygame.display.flip()
        continue

 
    if menu_org.game_state == "akt1":
        if current_scene is None:
            current_scene = act1
            game_state = "akt1"


    if not end_game:

        if current_scene:
            current_scene.update()


        if isinstance(current_scene, Akt_one):
            if current_scene.dialog.finished and not end_game:
                end_game = True
                close_time = pygame.time.get_ticks()

    sound.update(game_state)


    screen.fill((0, 0, 0))

    if not end_game:

        if current_scene:
            current_scene.draw(screen)

        settings.draw(screen)

    else:
        font = pygame.font.SysFont("arial", 40)

        text = font.render(
            "Піу-піу-піу крутий бoс файт всі програли)",
            True,
            (255, 255, 255)
        )

        rect = text.get_rect(center=screen.get_rect().center)
        screen.blit(text, rect)


        if close_time and pygame.time.get_ticks() - close_time > 5000:
            running = False

    pygame.display.flip()

pygame.quit()