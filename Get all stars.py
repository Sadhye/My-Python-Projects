import pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("Python/spacebg.jpg"), (WIDTH, HEIGHT))

pygame.display.set_caption("Get all stars")

def draw(drops):
    WIN.blit(BG, (0, 0))

    pygame.display.update()

def main():
    run = True

    drop_add_increment = 500
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for _ in range(3):
            drop_x = random.randint(0, WIDTH - DROP_WIDTH)
            drop = pygame.Rect(drop_x, -DROP_HEIGHT, DROP_WIDTH, DROP_HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(drops)

    pygame.quit()

if __name__ == "__main__":
    main()