import pygame
from random import randint, randrange

pygame.init()

# Вікно
WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змійка")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 64)

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

def new_game():
    # Дописати: спавн змії та їжі
    snake = []
    snake.append((100, 100))
    snake.append((80, 100))
    snake.append((60, 100))
    
    dx = BLOCK
    dy = 0
    
    food_x = randrange(0, WIDTH, BLOCK)
    food_y = randrange(0, HEIGHT, BLOCK)
    
    bad_food = []
    count = randint(1, 3)
    for i in range(count):
        x = randrange(0, WIDTH, BLOCK)
        y = randrange(0, HEIGHT, BLOCK)
        bad_food.append((x, y))
    
    score = 0
    game_over = False
    
    return snake, dx, dy, food_x, food_y, bad_food, score, game_over

snake, dx, dy, food_x, food_y, bad_food, score, game_over = new_game()




running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Дописати рух змії
            if not game_over:
                if event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -BLOCK
                if event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = BLOCK
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK
                    dy = 0
                if event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK
                    dy = 0


            if game_over and event.key == pygame.K_RETURN:
                # Перезапуск гри
                snake, dx, dy, food_x, food_y, bad_food, score, game_over = new_game()

    if not game_over:
        # Дописати логіку руху змії та умови програшу
        head_x = snake[0][0] + dx
        head_y = snake[0][1] + dy
        new_head = (head_x, head_y)
        
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True
        
        if new_head in snake:
            game_over = True
        
        snake.insert(0, new_head)
        
        remove_count = 1
        
        if head_x == food_x and head_y == food_y:
            score += 1
            food_x = randrange(0, WIDTH, BLOCK)
            food_y = randrange(0, HEIGHT, BLOCK)
            remove_count = 0
        
        for bf in bad_food:
            if head_x == bf[0] and head_y == bf[1]:
                remove_count = 2
                bad_food.remove(bf)
                break
        
        for i in range(remove_count):
            if len(snake) > 1:
                snake.pop()
        
        if len(bad_food) == 0:
            count = randint(1, 3)
            for i in range(count):
                x = randrange(0, WIDTH, BLOCK)
                y = randrange(0, HEIGHT, BLOCK)
                bad_food.append((x, y))



    # Малювання
    screen.fill(WHITE)

    for part in snake:
        pygame.draw.rect(screen, GREEN,
                         (part[0], part[1], BLOCK, BLOCK))

    pygame.draw.rect(screen, GREEN,
                     (food_x, food_y, BLOCK, BLOCK))

    for bf in bad_food:
        pygame.draw.rect(screen, RED,
                         (bf[0], bf[1], BLOCK, BLOCK))

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    if game_over:
        text1 = big_font.render("GAME OVER", True, RED)
        text2 = font.render("Натисни Enter для рестарту", True, BLACK)

        screen.blit(text1,
                    (WIDTH // 2 - text1.get_width() // 2,
                     HEIGHT // 2 - 50))
        screen.blit(text2,
                    (WIDTH // 2 - text2.get_width() // 2,
                     HEIGHT // 2 + 10))

    pygame.display.update()

pygame.quit()