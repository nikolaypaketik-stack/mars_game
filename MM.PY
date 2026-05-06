import pygame
from models.mini_games.audio.sound_manager import SoundManager
from models.mini_games.audio.settings import Settings
from models.mini_games.audio.audio_manager import AudioManager
from models.background.spase_background import SpaceBackground

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))

image_bg = pygame.image.load("assets/images/menu1.png").convert_alpha()
bg_rect = image_bg.get_rect(center=(640, 360))

start_button = pygame.Rect(340, 320, 200, 60)
exit_button = pygame.Rect(340, 640, 200, 60)

bass_area = pygame.Rect(950, 350, 120, 300)

audio = AudioManager()
settings = Settings(audio)
sound = SoundManager()

background = SpaceBackground()

game_state = "menu"
running = True


# -------- MENU --------
def handle_menu_events(event):
    global game_state, running

    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.collidepoint(event.pos):
            game_state = "game"

        if exit_button.collidepoint(event.pos):
            running = False


def update_menu():
    mouse_pos = pygame.mouse.get_pos()
    in_bass_zone = bass_area.collidepoint(mouse_pos)

    sound.update("menu", in_bass_zone)


def draw_menu():
    screen.blit(image_bg, bg_rect)
    settings.draw(screen)


# -------- GAME (АКТ 1) --------
def handle_game_events(event):
    global game_state

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game_state = "menu"


def update_game():
    background.update()
    sound.update("game", False)


def draw_game():
    background.draw(screen)


# -------- MAIN LOOP --------
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            handle_menu_events(event)
            settings.handle_event(event)

        elif game_state == "game":
            handle_game_events(event)

    if game_state == "menu":
        update_menu()
        draw_menu()

    elif game_state == "game":
        update_game()
        draw_game()

    pygame.display.update()

pygame.quit()