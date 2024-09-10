import pygame
import time
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Showdown")

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACESHIP_VEL = 5

BULLET_WIDTH, BULLET_HEIGHT = 10, 5
BULLET_VEL = 3
MAX_BULLETS = 5

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load("spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load("spaceship_red.png")  
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270 )

FONT = pygame.font.SysFont("comicsans", 30)
WINNING_FONT = pygame.font.SysFont("comicsans", 70)

def yellow_movement(keys, yellow):
    if keys[pygame.K_a] and yellow.x >= 0: # LEFT
        yellow.x -= SPACESHIP_VEL
    if keys[pygame.K_d] and yellow.x <= BORDER.x - SPACESHIP_WIDTH/2: # RIGHT
        yellow.x += SPACESHIP_VEL
    if keys[pygame.K_w] and yellow.y >= 0: # UP
        yellow.y -= SPACESHIP_VEL
    if keys[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_WIDTH: # DOWN
        yellow.y += SPACESHIP_VEL

def red_movement(keys, red):
    if keys[pygame.K_LEFT] and red.x >= BORDER.x: # LEFT
        red.x -= SPACESHIP_VEL
    if keys[pygame.K_RIGHT] and red.x <= WIDTH - SPACESHIP_WIDTH: # RIGHT
        red.x += SPACESHIP_VEL
    if keys[pygame.K_UP] and red.y >= 0: # UP
        red.y -= SPACESHIP_VEL
    if keys[pygame.K_DOWN] and red.y <= HEIGHT - SPACESHIP_HEIGHT: # DOWN
        red.y += SPACESHIP_VEL

def draw(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "black", BORDER)
    
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, "yellow", bullet)
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, "red", bullet)

    yellow_health_text = FONT.render(f"Yellow Health: {yellow_health}", 1, "yellow")
    WIN.blit(yellow_health_text, (10, 10))

    red_health_text = FONT.render(f"Red Health: {red_health}", 1, "red")
    WIN.blit(red_health_text, ((WIDTH - red_health_text.get_width()) - 10, 10))

    pygame.display.update()

def main():
    run = True

    clock = pygame.time.Clock()

    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_health = red_health = 10
    yellow_shot = red_shot = False

    yellow_bullets = []
    red_bullets = []

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        yellow_movement(keys, yellow)

        if keys[pygame.K_LSHIFT] and not yellow_shot and len(yellow_bullets) < 5:
            yellow_bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + SPACESHIP_HEIGHT/2, BULLET_WIDTH, BULLET_HEIGHT)
            yellow_bullets.append(yellow_bullet)
            yellow_shot = True
        if not keys[pygame.K_LSHIFT]:
            yellow_shot = False

        red_movement(keys, red)

        if keys[pygame.K_RSHIFT] and not red_shot and len(red_bullets) < 5:
            red_bullet = pygame.Rect(red.x, red.y + SPACESHIP_HEIGHT/2, BULLET_WIDTH, BULLET_HEIGHT)
            red_bullets.append(red_bullet)
            red_shot = True
        if not keys[pygame.K_RSHIFT]:
            red_shot = False

        for bullet in yellow_bullets[:]:
            bullet.x += BULLET_VEL
            if bullet.colliderect(red):
                red_health -= 1
                yellow_bullets.remove(bullet)
            if bullet.x > WIDTH:
                yellow_bullets.remove(bullet)
        
        for bullet in red_bullets[:]:
            bullet.x -= BULLET_VEL
            if bullet.colliderect(yellow):
                yellow_health -= 1
                red_bullets.remove(bullet)
            if bullet.x < 0:
                red_bullets.remove(bullet)
        
        if yellow_health <= 0:
            winning_text = WINNING_FONT.render("RED WINS!", 1, "red")
            WIN.blit(winning_text, (WIDTH/2 - winning_text.get_width()/2, HEIGHT/2 - winning_text.get_height()))
            pygame.display.update()
            pygame.time.delay(4000)
            main()
        
        if red_health <= 0:
            winning_text = WINNING_FONT.render("YELLOW WINS!", 1, "yellow")
            WIN.blit(winning_text, (WIDTH/2 - winning_text.get_width()/2, HEIGHT/2 - winning_text.get_height()))
            pygame.display.update()
            pygame.time.delay(4000)
            main()
        
        draw(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health)
    
    pygame.quit()

if __name__ == "__main__":
    main()