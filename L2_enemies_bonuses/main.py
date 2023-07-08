import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

COLORS = [(255, 255, 255), (255, 160, 122), (255, 255, 0), (147, 112, 219)]

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = 5

def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():
    bonus = pygame.Surface((20, 20))
    bonus.fill(GREEN)
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
enemies = []

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 1500)
bonuses = []

score = 0

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)

    # process hero movement
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_DOWN] and not ball_rect.bottom + ball_speed > height:
        ball_rect = ball_rect.move(0, ball_speed)
    if pressed_keys[K_UP] and not ball_rect.top - ball_speed < 0:
        ball_rect = ball_rect.move(0, -ball_speed)
    if pressed_keys[K_RIGHT] and not ball_rect.right + ball_speed > width:
        ball_rect = ball_rect.move(ball_speed, 0)
    if pressed_keys[K_LEFT] and not ball_rect.left - ball_speed < 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    # process enemies
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    # process bonuses
    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))
        else:
            if ball_rect.colliderect(bonus[1]):
                bonuses.pop(bonuses.index(bonus))
                score = score + 1
                print('Your score:', score)

    pygame.display.flip()
