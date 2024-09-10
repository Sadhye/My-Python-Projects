import pygame
import time
pygame.font.init()

WIDTH, HEIGHT = 900, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))
pygame.display.set_caption("Race")

PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40

PLAYER_GO_VEL = 50
PLAYER_BACK_VEL = 5

YELLOW_IMAGE = pygame.image.load("spaceship_yellow.png")
YELLOW = pygame.transform.rotate(pygame.transform.scale(YELLOW_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90)

RED_IMAGE = pygame.image.load("spaceship_red.png")
RED = pygame.transform.rotate(pygame.transform.scale(RED_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90)

FINISH_LINE = pygame.Rect(800, 0, 5, HEIGHT)

COUNTDOWN_FONT = pygame.font.SysFont("comicsans", 150)
WINNING_FONT = pygame.font.SysFont("comicsans", 80)

def countdown():
    count = ["3", "2", "1"]
    go = COUNTDOWN_FONT.render("GO!", 1, "white")
    go_list = [go]
    
    for i in count.copy():
        countdown = COUNTDOWN_FONT.render(f"{count[0]}", 1, "white")
        WIN.blit(countdown, (WIDTH/2 - countdown.get_width()/2, HEIGHT/2 - countdown.get_height()/2))
        pygame.display.update()
        pygame.time.delay(1000)
        count.remove(i)
    
    for go in go_list.copy():
        WIN.blit(go, (WIDTH/2 - go.get_width()/2, HEIGHT/2 - go.get_height()/2))
        pygame.display.update()
    
    start_time = time.time()
    end_time = time.time() - start_time

    if int(end_time) == 1:
        go_list.remove(go)

def draw(yellow, red):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "red", FINISH_LINE)

    WIN.blit(YELLOW, (yellow.x, yellow.y))
    WIN.blit(RED, (red.x, red.y))

    pygame.display.update()

def main():
    run = True

    yellow = pygame.Rect(100, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    red = pygame.Rect(100, 100, PLAYER_WIDTH, PLAYER_HEIGHT)

    yellow_go = red_go = False

    clock = pygame.time.Clock()

    countdown()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        if yellow.x > 100:
            yellow.x -= PLAYER_BACK_VEL
        
        if red.x > 100:
            red.x -= PLAYER_BACK_VEL
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] and not yellow_go:
            yellow.x += PLAYER_GO_VEL
            yellow_go = True
        if not keys[pygame.K_LSHIFT]:
            yellow_go = False

        if keys[pygame.K_RSHIFT] and not red_go:
            red.x += PLAYER_GO_VEL
            red_go = True
        if not keys[pygame.K_RSHIFT]:
            red_go = False
        
        if yellow.x + PLAYER_WIDTH >= FINISH_LINE.x:
            winning_text = WINNING_FONT.render("YELLOW WINS!", 1, "yellow")
            WIN.blit(winning_text, (WIDTH/2 - winning_text.get_width()/2, HEIGHT/2 - winning_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            main()
        
        if red.x + PLAYER_WIDTH >= FINISH_LINE.x:
            winning_text = WINNING_FONT.render("RED WINS!", 1, "red")
            WIN.blit(winning_text, (WIDTH/2 - winning_text.get_width()/2, HEIGHT/2 - winning_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            main()
        
        draw(yellow, red)
    
    pygame.quit()

if __name__ == "__main__":
    main()