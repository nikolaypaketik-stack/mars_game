import pygame

class Menu:

    def __init__(self):
        self.start_button = pygame.Rect(340, 320, 200, 60)
        self.participants_button = pygame.Rect(340, 480, 200, 60)
        self.exit_button_in_menu = pygame.Rect(340, 640, 200, 60)

        self.bass_area = pygame.Rect(950, 350, 120, 300)
        self.tv_area = pygame.Rect(160, 360, 300, 200)

        self.akt = 1

        self.in_bass_zone = False
        self.in_tv_zone = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.start_button.collidepoint(event.pos):
                self.akt += 1
                return "game_akt_one"

            elif self.participants_button.collidepoint(event.pos):
                return "participants"

            elif self.exit_button_in_menu.collidepoint(event.pos):
                return "exit"

        return None

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        self.in_bass_zone = self.bass_area.collidepoint(mouse_pos)
        self.in_tv_zone = self.tv_area.collidepoint(mouse_pos)

    def draw(self, screen):
        pass