import pygame
import random
import time

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("rainbg.jpeg"), (WIDTH, HEIGHT))

pygame.display.set_caption("Rain Effect")

DROP_WIDTH = 2
DROP_HEIGHT = 15
DROP_VEL = 10

def draw(drops):
    WIN.blit(BG, (0, 0))

    for drop in drops:
        pygame.draw.rect(WIN, "blue", drop)

    pygame.display.update()

def main():
    run = True

    drops_add_increment = 500
    drops = []
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        for _ in range(3):
            drop_x = random.randint(0, WIDTH - DROP_WIDTH)
            drop = pygame.Rect(drop_x, -DROP_HEIGHT, DROP_WIDTH, DROP_HEIGHT)
            drops.append(drop)
        
        for drop in drops[:]:
            drop.y += DROP_VEL
            if drop.y > HEIGHT:
                drops.remove(drop)
        
        draw(drops)
    
    pygame.quit()

if __name__ == "__main__":
    main()