import pygame
import time
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
snake = [(3, 3), (2, 3), (1, 3)]
snake_direction = (1, 0)

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game variables
score = 0
running = True

# Define the function to reset the game
def reset_game():
    global snake, snake_direction, food, score, running
    snake = [(3, 3), (2, 3), (1, 3)]
    snake_direction = (1, 0)
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    score = 0
    running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    if keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    if keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Move the snake
    new_head = (
        (snake[0][0] + snake_direction[0]) % GRID_WIDTH,
        (snake[0][1] + snake_direction[1]) % GRID_HEIGHT
    )
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for self-collisions
    if snake[0] in snake[1:]:
        running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the food
    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Draw the snake head (larger and different color)
    pygame.draw.rect(
        screen, (0, 100, 0), (snake[0][0] * GRID_SIZE, snake[0][1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Game over
font = pygame.font.Font(None, 36)
text = font.render(f"Game Over - Score: {score}", True, WHITE)
text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a few seconds before quitting or resetting
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
