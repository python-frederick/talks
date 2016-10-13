import pygame
import random

class Direction:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 4

def main():
    pygame.init()
    clock = pygame.time.Clock()

    (width, height) = (640, 480)
    black = pygame.Color('black')
    green = pygame.Color('green')
    red = pygame.Color('red')

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake')
    screen.fill(black)
    pygame.display.update()

    cell = 16
    nx, ny = width / cell, height / cell
    mid = nx * ny / 2 + nx / 2
    snake = [mid, mid + nx, mid + 2*nx, mid + 3*nx]
    direction = Direction.UP
    lapsed = 0
    delay = 50
    apple = random.randint(0, nx * ny)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    direction = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    direction = Direction.RIGHT

        lapsed += clock.get_time()
        if lapsed >= delay:
            lapsed = 0
            if direction == Direction.UP:
                head = snake[0] - nx
            elif direction == Direction.DOWN:
                head = snake[0] + nx
            elif direction == Direction.LEFT:
                head = snake[0] - 1
            elif direction == Direction.RIGHT:
                head = snake[0] + 1

            if head in snake:
                running = False

            if head == apple:
                apple = random.randint(0, nx * ny)
                snake = [head] + snake
            else:
                snake = [head] + snake[:-1]

        screen.fill(black)

        x = (apple % nx) * cell + 1
        y = (apple / nx) * cell + 1
        rect = pygame.Rect(x, y, cell - 2, cell - 2)
        screen.fill(red, rect)

        for part in snake:
            x = (part % nx) * cell + 1
            y = part / nx * cell + 1
            rect = pygame.Rect(x, y, cell - 2, cell - 2)
            screen.fill(green, rect)

        pygame.display.update()

        # give some time back to CPU
        pygame.time.wait(5)
        clock.tick(60)   # max FPS = 30

if __name__ == '__main__':
    main()
