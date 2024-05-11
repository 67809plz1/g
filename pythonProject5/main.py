import pygame
import random

b1_clock = pygame.time.Clock()
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

d = pygame.image.load('gg/stoit.png')

place = pygame.image.load('levels/lev1.png')
walk_left = [pygame.image.load('gg/stoit left.png'),
             pygame.image.load('gg/left 1.png'),
             pygame.image.load('gg/left 2.png')
 ]

walk_right = [pygame.image.load('gg/stoit.png'),
             pygame.image.load('gg/stoit 1.png'),
             pygame.image.load('gg/stoit 2.png')
 ]

b1 =[pygame.image.load('bug/b1.png'),
     pygame.image.load('bug/b2.png'),
     pygame.image.load('bug/b3.png')
]
b1_x = 700
b1_y = 400

player_anim_count = 0
b1_aim_count = 0

player_speed = 5
player_x = 200
player_y = 400

jump = False
jump_count = 8

running = True
while running:

    screen.blit(place, (0, 0))
    screen.blit(b1[b1_aim_count],(b1_x, b1_y))

    player_r = walk_right[0].get_rect(topleft = (player_x, player_y))
    b1_r = b1.get_rect(topleft= (b1_x, 400))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
       screen.blit(walk_left[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_RIGHT]:
       screen.blit(walk_right[player_anim_count], (player_x, player_y))
    else:
        screen.blit(d, (player_x, player_y))


    if keys[pygame.K_LEFT] and player_x > 10:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed

    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= ( jump_count ** 2) / 2
            else:
                player_y += ( jump_count ** 2) / 2
            jump_count -= 1
        else:
            jump = False
            jump_count = 8

    if player_anim_count == 2:
       player_anim_count = 0
    else:
        player_anim_count +=1

    if b1_aim_count == 2:
       b1_aim_count = 0
    else:
        b1_aim_count +=1



    b1_x -= 3
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


    clock.tick(60)