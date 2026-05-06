import pygame
from models.mini_games.audio.sound_manager import SoundManager
from models.mini_games.audio.settings import Settings
from models.mini_games.audio.audio_manager import AudioManager

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))

image_bg = pygame.image.load("assets/images/menu1.png").convert_alpha()
bg_rect = image_bg.get_rect(center=(640, 360))

start_button = pygame.Rect(660, 320, 200, 60)



start_button = pygame.Rect(340, 320, 200, 60)
participants_button = pygame.Rect(340, 480, 200, 60)
exit_button = pygame.Rect(340, 640, 200, 60)
bass_area = pygame.Rect(950, 350, 120, 300)
tv_area = pygame.Rect(160, 360, 300, 200)

audio = AudioManager()
settings = Settings(audio)

sound = SoundManager()
game_state = "menu"

running = True
while running:

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_state = "game"

            if exit_button.collidepoint(event.pos):
                running = False

        # ✔ важно: сюда же добавляем настройки
        settings.handle_event(event)

    # mouse
    mouse_pos = pygame.mouse.get_pos()
    in_bass_zone = bass_area.collidepoint(mouse_pos)

    sound.update(game_state, in_bass_zone)

    # screen
    screen.blit(image_bg, bg_rect)

    # ✔ рисуем настройки
    settings.draw(screen)

    pygame.display.update()

pygame.quit()