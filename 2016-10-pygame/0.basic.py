import pygame

def main():
    pygame.init()

    black = pygame.Color('black')

    (width, height) = (640, 480)
    screen = pygame.display.set_mode((width, height))
    screen.fill(black)
    pygame.display.update()

    clock = pygame.time.Clock()

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()
