import pygame
import random

pygame.init()
pygame.font.init()

# const
SIZE = (700, 600)
RED = (200, 0, 0)
GREY = (220, 220, 220)
DARK_GREY = (120, 120, 120)
GREEN = (100, 200, 100)
FPS = 60

SPAWN_ENEMY = pygame.USEREVENT + 1

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Dino')

clock = pygame.time.Clock()

hero = {
    'x': 40,
    'y': 300,
    'speed': 15
}

is_jump = False

enemy_pos = [[SIZE[0], 300]]
pygame.time.set_timer(SPAWN_ENEMY, 1200)
enemy_speed = 5


def jump(y, speed):
    y -= speed

    if y > 290:
        global is_jump
        is_jump = False

        hero['y'] = 300
        hero['speed'] = 15

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
            if event.type == SPAWN_ENEMY:
                enemy_pos.append([SIZE[0], 300])

        if is_jump:
            hero['y'] = jump(hero['y'], hero['speed'])
            hero['speed'] -= 1

        screen.fill(GREY)

        for i in enemy_pos:
            i[0] -= enemy_speed

            # check enemy_pos and hero_pos
            if i[0] in range(hero['x'], hero['x'] + 15) and i[1] in range(hero['y'], hero['y'] + 40):
                pygame.time.delay(1000)
                quit()

            pygame.draw.rect(screen, GREEN, (i[0], i[1], 10, 40))

        pygame.draw.rect(screen, RED, (hero['x'], hero['y'], 15, 40))
        pygame.draw.rect(screen, DARK_GREY, (0, 340, SIZE[0], SIZE[1]))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
