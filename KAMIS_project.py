import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 1200, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
xb = 150
yb = 250
x = 1200

positions = [630, 530, 430]
fr_position = random.choice(positions)
number = 0


endx = x + 300
endy = fr_position + 500

# font
font = pygame.font.SysFont("comicsans", 70)
num_font = pygame.font.SysFont("comicsans", 90)

# set up game loop
run = 0
start = False
FPS = 60
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (51, 176, 255)


images = [pygame.image.load("pillar.png"), pygame.image.load("bird.png")]


upper_pillar = pygame.transform.flip(images[0], False, True)

Time = time.time()


def main_menu():
    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, (548, 295, 105, 85), 7)  # 558 85
    # pygame.surface.fill()
    pygame.draw.polygon(
        win, BLACK, [(573, 310), (573, 365), (630, 337)], 5)
    pygame.display.update()


def score():
    text = num_font.render(str(number), 1, WHITE)
    win.blit(text, (WIDTH/2 - text.get_width() / 2, 100))
    pygame.display.update()


def display_massage(massage):
    win.fill(BLACK)
    text = font.render(massage, 1, WHITE)
    win.blit(text, (WIDTH/2 - text.get_width() /
                    2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)


def pillar_p():
    win.blit(images[0], (x, fr_position))


def upper_pillar_p():
    win.blit(upper_pillar, (x, fr_position - 750))


while run == 0:
    main_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_m, y_m = pygame.mouse.get_pos()
            if 563 < x_m < 638 and 263 < y_m < 338:
                run += 1
                start = True


while start:

    start_time = time.time()
    passed_time = int(start_time - Time)
    seconds = []
    seconds.append(passed_time)
    score()

    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    if (x - 180) <= xb and (fr_position - 100) <= yb:
        display_massage("you lost")
        start = False
        break
    elif (x - 180) <= xb and (fr_position - 350) >= yb:
        display_massage("you lost")
        start = False
        break
    if xb == x:
        number += 1

    for second in seconds:

        if keys[pygame.K_SPACE]:
            yb -= 10
            yb -= 7
            yb -= 5

        if yb < 700:
            yb += 5
        elif yb == 700:
            display_massage("you lost")
            start = False
            break

        x -= 5
        if x == 0:
            x += 1200
            r_position = random.choice(positions)
            fr_position = r_position

    win.fill(BLUE)
    pillar_p()
    upper_pillar_p()

    win.blit(images[1], (xb, yb))
    pygame.display.update()


pygame.quit
