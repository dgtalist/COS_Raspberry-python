import motor_module as motor
import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("AI car")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                turnLeft()
            if event.key == pygame.K_RIGHT:
                turnRight()
            if event.key == pygame.K_UP:
                forward_l()
            if event.key == pygame.K_DOWN:
                Reverse()
        if event.type == pygame.KEYUP:
            stop()
