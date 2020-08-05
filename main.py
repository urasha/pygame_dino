import pygame
import random

pygame.init()
pygame.font.init()

# const
SIZE = (700, 600)
RED = (200, 0, 0)
GREY = (220, 220, 220)
DARK_GREY = (120, 120, 120)
GREEN = (0, 255, 0)
FPS = 60

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Dino')

clock = pygame.time.Clock()

hero = {
    'x': 40,
    'y': 300,
    'speed': 14
}

is_jump = False


def jump(y, speed):
    y -= speed

    if y > 290:
        global is_jump
        is_jump = False

        hero['y'] = 300
        hero['speed'] = 14

    return y


def main():
    global is_jump

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jump = True

        if is_jump:
            hero['y'] = jump(hero['y'], hero['speed'])
            hero['speed'] -= 1

        screen.fill(GREY)

        pygame.draw.rect(screen, RED, (hero['x'], hero['y'], 15, 40))
        pygame.draw.rect(screen, DARK_GREY, (0, 340, SIZE[0], SIZE[1]))
        pygame.draw.rect(screen, GREEN, (60, 300, 10, 40))  #test

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
