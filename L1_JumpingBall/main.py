import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random

pygame.init()

#FPS = pygame.time.Clock()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0

COLORS = [(255, 255, 255), (255, 160, 122), (255, 255, 0), (147, 112, 219)]

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        color = COLORS[random.randint(0, len(COLORS) - 1)]
        ball.fill(color)
    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_speed[0] = -ball_speed[0]
        color = COLORS[random.randint(0, len(COLORS) - 1)]
        ball.fill(color)

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)

    pygame.display.flip()
