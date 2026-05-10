import pygame

class PlayerMove:

    def __init__(self, screen):
        self.speed = 2

        self.rect = pygame.Rect(0, 0, 50, 50)


        self.rect.center = screen.get_rect().center
        self.history = []
        self.target_center = None

    def move_to_center(self, screen):
        cx, cy = screen.get_rect().center
        dx = cx - self.rect.centerx
        dy = cy - self.rect.centery

        self.rect.x += dx * 0.03
        self.rect.y += dy * 0.03

    def update(self, force_center=False):
        keys = pygame.key.get_pressed()

        if not force_center:
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            if keys[pygame.K_s]:
                self.rect.y += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed

        self.history.append((self.rect.x, self.rect.y))


        if self.rect.left < 0:
            self.rect.left = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
