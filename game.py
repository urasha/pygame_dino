import pygame
import random

pygame.init()
pygame.font.init()

# const
SIZE = (600, 400)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Dino')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
