import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("spacebgbg.jpg"), (WIDTH, HEIGHT))
pygame.display.set_caption("Blaster Game")

PLAYER_WIDTH = 60
PLAYER_HEIGHT = 80
PLAYER_VEL = 7

ASTEROID_WIDTH = 70
ASTEROID_HEIGHT = 70
ASTEROID_VEL = 2

BLASTER_WIDTH = 40
BLASTER_HEIGHT = 40
BLASTER_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, asteroids, elapsed_time, blasters):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)
    
    for asteroid in asteroids:
        pygame.draw.rect(WIN, "grey", asteroid)
    
    for blaster in blasters:
        pygame.draw.rect(WIN, "brown", blaster)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    player = pygame.Rect(int(WIDTH/2), HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    asteroid_add_increment = 2000
    asteroids = []
    asteroid_count = 0
    hit = False
    hit_ground = False
    shot = False
    blasters = []

    start_time = time.time()

    while run:
        asteroid_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_SPACE] and not shot:
            blaster = pygame.Rect(player.x + 20, player.y + PLAYER_HEIGHT, BLASTER_WIDTH, BLASTER_HEIGHT)
            blasters.append(blaster)
            shot = True
            pygame.display.update()
        elif not keys[pygame.K_SPACE]:
            shot = False
        
        if asteroid_count > asteroid_add_increment:
            for _ in range(1):
                asteroid_x = random.randint(0, WIDTH - ASTEROID_WIDTH)
                asteroid = pygame.Rect(asteroid_x, -ASTEROID_HEIGHT, ASTEROID_WIDTH, ASTEROID_HEIGHT)
                asteroids.append(asteroid)
            
            asteroid_add_increment = max(200, asteroid_add_increment - 50)
            asteroid_count = 0
        
        for blaster in blasters.copy():
            blaster.y -= BLASTER_VEL
            for asteroid in asteroids[:]:
                if blaster.colliderect(asteroid):
                    asteroids.remove(asteroid)
                    blasters.remove(blaster)
            if blaster.y < 0:
                blasters.remove(blaster)
        
        for asteroid in asteroids[:]:
            asteroid.y += ASTEROID_VEL
            if asteroid.y > HEIGHT:
                hit_ground = True
                break
            elif asteroid.y + asteroid.height >= player.y and asteroid.colliderect(player):
                hit = True
                break
        
        if hit_ground:
            lost_text = FONT.render(f"Oh no! You didn't hit an asteroid. You lasted {round(elapsed_time)}s", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_width()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = True
            hit = False
            hit_ground = False
            asteroids = []
            blasters = []
            asteroid_add_increment = 2000
            asteroid_count = 0
            player.x = int(WIDTH/2)
            start_time = time.time()
        
        if hit:
            lost_text = FONT.render(f"Oh no! An asteroid hit you. You lasted {round(elapsed_time)}s", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_width()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = True
            hit = False
            hit_ground = False
            asteroids = []
            blasters = []
            asteroid_add_increment = 2000
            asteroid_count = 0
            player.x = int(WIDTH/2)
            start_time = time.time()

        draw(player, asteroids, elapsed_time, blasters)
    
    pygame.quit()

if __name__ == "__main__":
    main()