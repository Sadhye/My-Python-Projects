import pygame
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))
pygame.display.set_caption("Pong Throw")

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACESHIP_VEL = 5.2

YELLOW_SPACESHIP_IMAGE = pygame.image.load("spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load("spaceship_red.png")  
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

BALL_SIDE = 18
BALL_VEL = 6

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

def yellow_movement(keys, yellow):
    if keys[pygame.K_w] and yellow.y >= 0: # UP
        yellow.y -= SPACESHIP_VEL

    if keys[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_WIDTH: # DOWN
        yellow.y += SPACESHIP_VEL
    
    if keys[pygame.K_a] and yellow.x >= 0: # LEFT
        yellow.x -= SPACESHIP_VEL
    
    if keys[pygame.K_d] and yellow.x <= BORDER.x - SPACESHIP_WIDTH/2:
        yellow.x += SPACESHIP_VEL

def red_movement(keys, red):
    if keys[pygame.K_LEFT] and red.x >= BORDER.x: # LEFT
        red.x -= SPACESHIP_VEL

    if keys[pygame.K_RIGHT] and red.x <= WIDTH - SPACESHIP_WIDTH: # RIGHT
        red.x += SPACESHIP_VEL

    if keys[pygame.K_UP] and red.y >= 0: # UP
        red.y -= SPACESHIP_VEL

    if keys[pygame.K_DOWN] and red.y <= HEIGHT - SPACESHIP_HEIGHT: # DOWN
        red.y += SPACESHIP_VEL

def draw(yellow, red, ball):
    WIN.blit(BG, (0, 0))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    pygame.draw.rect(WIN, "black", BORDER)

    pygame.draw.rect(WIN, "white", ball)

    pygame.display.update()

def main():
    run = True

    clock = pygame.time.Clock()

    yellow = pygame.Rect(100, HEIGHT/2 - SPACESHIP_HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, HEIGHT/2 - SPACESHIP_HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    ball = pygame.Rect(WIDTH/2 - BALL_SIDE/2, HEIGHT/2 - BALL_SIDE/2, BALL_SIDE, BALL_SIDE)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()

        yellow_movement(keys, yellow)
        red_movement(keys, red)

        if ball.colliderect(yellow):
            ball.x = yellow.x + SPACESHIP_WIDTH/2
            ball.y = yellow.y + SPACESHIP_HEIGHT/2

        elif ball.colliderect(red):
            ball.x = red.x - BALL_SIDE
            ball.y = red.y + SPACESHIP_HEIGHT/2
        
        draw(yellow, red, ball)
    
    pygame.quit()

if __name__ == "__main__":
    main()