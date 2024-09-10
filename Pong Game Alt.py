import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
BG = pygame.transform.scale(pygame.image.load("Python/Black Screen.jpg"), (WIDTH, HEIGHT))

PLAYERS_WIDTH = 40
PLAYERS_HEIGHT = 60
PLAYERS_VEL = 5
BALL_VEL = 5  # Define BALL_VEL before the loop
BALL_SIDE = 25

def draw(player_blue, player_red, ball):
    WIN.blit(BG, (0, 0))
    
    pygame.draw.rect(WIN, "blue", player_blue)
    pygame.draw.rect(WIN, "red", player_red)
    pygame.draw.rect(WIN, "white", ball)
    
    pygame.display.update()

def main():
    run = True
    
    player_blue = pygame.Rect(int(WIDTH/2), HEIGHT - PLAYERS_HEIGHT, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    player_red = pygame.Rect(int(WIDTH/2), 0, PLAYERS_WIDTH, PLAYERS_HEIGHT)
    ball = pygame.Rect(int(WIDTH/2), int(HEIGHT/2), BALL_SIDE, BALL_SIDE)
    
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_blue.x - PLAYERS_VEL >= 0:
            player_blue.x -= PLAYERS_VEL
        if keys[pygame.K_RIGHT] and player_blue.x + PLAYERS_VEL + player_blue.width <= WIDTH:
            player_blue.x += PLAYERS_VEL
        if keys[pygame.K_a] and player_red.x - PLAYERS_VEL >= 0:
            player_red.x -= PLAYERS_VEL
        if keys[pygame.K_d] and player_red.x + PLAYERS_VEL + player_red.width <= WIDTH:
            player_red.x += PLAYERS_VEL
        
        # Update ball position and handle collision with player_blue or edges
        ball.y += BALL_VEL
        if ball.colliderect(player_blue) or ball.top <= 0 or ball.bottom >= HEIGHT:
            BALL_VEL *= -1  # Reverse the direction of the ball (consider bouncing off top and bottom edges)

        draw(player_blue, player_red, ball)
            
    pygame.quit()

if __name__ == "__main__":
    main()