import pygame
import random

# Define game parameters
WIDTH = 800
HEIGHT = 600
SNAKE_SIZE = 20
SNAKE_SPEED = 10
FOOD_SIZE = 10

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define initial snake position and direction
snake_pos = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = pygame.K_RIGHT

# Create food at a random position
food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))

# Game loop
running = True
while running:
    # Check for user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Change snake direction based on key press
            if event.key == pygame.K_LEFT and snake_direction != pygame.K_RIGHT:
                snake_direction = pygame.K_LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != pygame.K_LEFT:
                snake_direction = pygame.K_RIGHT
            elif event.key == pygame.K_UP and snake_direction != pygame.K_DOWN:
                snake_direction = pygame.K_UP
            elif event.key == pygame.K_DOWN and snake_direction != pygame.K_UP:
                snake_direction = pygame.K_DOWN

    # Update snake position based on direction
    new_head_pos = (snake_pos[0][0] + SNAKE_SPEED * {
        pygame.K_LEFT: -1,
        pygame.K_RIGHT: 1,
        pygame.K_UP: 0,
        pygame.K_DOWN: 0
    }[snake_direction], snake_pos[0][1] + SNAKE_SPEED * {
        pygame.K_LEFT: 0,
        pygame.K_RIGHT: 0,
        pygame.K_UP: -1,
        pygame.K_DOWN: 1
    }[snake_direction])

    # Check for collision with food
    if new_head_pos == food_pos:
        # Eat food, grow snake, and spawn new food
        snake_pos.insert(0, new_head_pos)
        food_pos = (random.randint(0, WIDTH - FOOD_SIZE), random.randint(0, HEIGHT - FOOD_SIZE))
    else:
        # Move snake body
        snake_pos.insert(0, new_head_pos)
        snake_pos.pop()

    # Check for collision with self or walls
    if new_head_pos in snake_pos[1:] or new_head_pos[0] < 0 or new_head_pos[0] >= WIDTH or new_head_pos[1] < 0 or new_head_pos[1] >= HEIGHT:
        running = False

    # Fill screen and draw snake and food
    screen.fill(BLACK)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
