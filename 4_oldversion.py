import pygame  
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

backgroundImage = pygame.image.load('backgr.jpg')

playerImage = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_dx = 0

enemyImage = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_dx = 4
enemy_dy = 0

bulletImage = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_dx = 0
bullet_dy = 10
bullet_m = 'ready'

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def fire_bullet(x, y):
    global bullet_m
    bullet_m = 'fire'
    screen.blit(bulletImage, (x + 16, y + 10))

def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    dis = math.sqrt(math.pow(enemy_x - bullet_x,2) + math.pow(enemy_y - bullet_y,2))
    if dis < 27:
        return True
    else:
        return False


while running: 
    screen.fill((0, 0, 0))
    screen.blit(backgroundImage, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: 
        player_x -= 5
    if pressed[pygame.K_RIGHT]: 
        player_x += 5
    if pressed[pygame.K_SPACE]: 
        if bullet_m is 'ready':
            bullet_x = player_x
            fire_bullet(player_x, bullet_y)
   
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_dx = 0
    

    player_x += player_dx
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    enemy_x += enemy_dx
    if enemy_x <= 0:
        enemy_dx = 4
        enemy_y += enemy_dy
    elif enemy_x >= 736:
        enemy_dx = -4
        enemy_y -= enemy_dy

    if bullet_y <=0:
        bullet_y = 480
        bullet_m = 'ready'
    if bullet_m is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_dy

    coll = collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if coll:
        bullet_y = 480
        bullet_m = 'ready'
        enemy_x = random.randint(0, 735)
        enemy_y = random.randint(50, 150)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()


    pygame.display.flip()
