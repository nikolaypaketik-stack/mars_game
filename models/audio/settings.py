import pygame

class AudioSettings:
    def __init__(self, audio):
        self.audio = audio

        self.volume = 0.5

        self.start_x = 50
        self.width = 200

        self.volume_bar = pygame.Rect(self.start_x, 650, self.width, 10)
        self.knob = pygame.Rect(self.start_x, 645, 10, 20)

    def handle_event(self, event):
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            if pygame.mouse.get_pressed()[0]:
                if self.volume_bar.collidepoint(event.pos):

                    
                    self.volume = (event.pos[0] - self.start_x) / self.width
                    self.volume = max(0.0, min(1.0, self.volume))

                   
                    self.audio.set_music_volume(self.volume)

    def draw(self, screen):
        pygame.draw.rect(screen, (80, 80, 80), self.volume_bar)

        self.knob.x = self.start_x + int(self.volume * self.width)
        pygame.draw.rect(screen, (200, 200, 200), self.knob)
        
