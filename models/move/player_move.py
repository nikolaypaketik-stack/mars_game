import pygame

class PlayerMove:

    def __init__(self):
        self.speed = 1.2
        self.rect = pygame.Rect(100, 100, 50, 50)

        #self.image = pygame.image.load("assets/images/ship/spaseship1.1.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image, (120, 120))
        #self.rect = self.image.get_rect(center=(640, 360))

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
        #screen.blit(self.image, self.rect)
