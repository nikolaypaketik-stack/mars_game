import pygame

class PlayerMove:

    def __init__(self, screen):
        self.speed = 2

        self.rect = pygame.Rect(0, 0, 50, 50)

        # FIX: используем screen только один раз, без хранения зависимости
        self.rect.center = screen.get_rect().center

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
