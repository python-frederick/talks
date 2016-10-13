import pygame

def main():
    pygame.init()

    black = pygame.Color('black')
    white = pygame.Color('white')

    (width, height) = (640, 480)
    screen = pygame.display.set_mode((width, height))
    screen.fill(black)
    pygame.display.update()

    clock = pygame.time.Clock()

    x, y = width / 2, height / 2
    radius = 32

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(black)
        pygame.draw.circle(screen, white, (x, y), radius)
        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()
