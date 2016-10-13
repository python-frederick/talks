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

    (width, height) = (320, 320)
    black = pygame.Color('black')
    green = pygame.Color('green')
    red = pygame.Color('red')

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake')
    screen.fill(black)
    pygame.display.update()

    cell = 16
    nx, ny = width / cell, height / cell
    def get_rect(index):
        x = (index % nx) * cell + 1
        y = (index / nx) * cell + 1
        return pygame.Rect(x, y, cell - 2, cell - 2)

    mid = nx * ny / 2 + nx / 2
    snake = [mid, mid + nx, mid + 2*nx, mid + 3*nx]
    direction = Direction.UP

    apple = random.randint(0, nx * ny)
    screen.fill(red, get_rect(apple))

    dirty = snake + [apple]

    lapsed = 0
    delay = 100

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
                dirty.append(apple)
                apple = random.randint(0, nx * ny)
                screen.fill(red, get_rect(apple))
                dirty.append(apple)
                snake = [head] + snake
            else:
                tail = snake[-1]
                screen.fill(black, get_rect(tail))
                dirty.append(tail)
                snake = [head] + snake[:-1]
            screen.fill(green, get_rect(head))
            dirty.append(head)


        pygame.display.update([get_rect(idx) for idx in dirty])

        # give some time back to CPU
        pygame.time.wait(5)
        clock.tick(60)   # max FPS = 30

if __name__ == '__main__':
    main()
