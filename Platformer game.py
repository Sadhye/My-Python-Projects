import pygame
import time

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

BG = pygame.transform.scale(pygame.image.load("Python/platformerbg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
PLAYER_JUMPVEL = 30

def draw(player, platform1, platform2):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "red", player)
    
    pygame.draw.rect(WIN, "green", platform1) #platform 1
    pygame.draw.rect(WIN, "green", platform2) #platform 2
    
    pygame.display.update()

def main():
    run = True
    
    player = pygame.Rect(10, 598, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    platform1 = pygame.Rect(800, 548, 60, 10)
    platform2 = pygame.Rect(600, 528, 60, 10)
    
    clock = pygame.time.Clock()
    is_jumping = False
    jump_count = 10
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        
        if not is_jumping:
            if keys[pygame.K_UP]:
                is_jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player.y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10
        
        if player.y >= 598:
            player.y = 598
        
        draw(player, platform1, platform2)
    
    pygame.quit()

if __name__ == "__main__":
    main()