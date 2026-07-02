import pygame
import random

# start pygame
pygame.init()

# screen size
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# colors (R, G, B)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# size of one block
BLOCK = 20

# speed of game
clock = pygame.time.Clock()
speed = 10

# font for score and messages
font = pygame.font.SysFont("arial", 25)


def show_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [5, 5])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK, BLOCK])


def game_loop():
    game_over = False

    # snake starting position (middle of screen)
    x = WIDTH / 2
    y = HEIGHT / 2

    # how much snake moves each step
    x_change = 0
    y_change = 0

    snake_list = []   # list of all body parts
    snake_length = 1

    # food starting position (random spot)
    food_x = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
    food_y = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # change direction when arrow key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK
                    x_change = 0

        # move snake
        x += x_change
        y += y_change

        # check if snake hit the wall
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        # draw background
        screen.fill(BLACK)

        # draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK, BLOCK])

        # add new head position to snake body
        snake_head = [x, y]
        snake_list.append(snake_head)

        # remove extra tail part if snake didn't grow
        if len(snake_list) > snake_length:
            del snake_list[0]

        # check if snake hit itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # check if snake ate the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
            food_y = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()


game_loop()
