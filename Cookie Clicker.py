import pygame

WIDTH, HEIGHT = 500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

COOKIE_IMAGE = pygame.image.load("cookie.png")
COOKIE = pygame.transform.scale(COOKIE_IMAGE, (30, 30))
#cookie = pygame.Rect()

def draw(cookie):
    pass

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == "__main__":
    main()