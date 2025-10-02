import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background1.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))  # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    
    # Background Image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Player movement
    playerX += playerX_change
    
    # Boundary checking for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH - 64:  # 64 is player width
        playerX = SCREEN_WIDTH - 64
    
    # Enemy movement
    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            break
            
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = ENEMY_SPEED_X
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] = -ENEMY_SPEED_X
            enemyY[i] += enemyY_change[i]
    
    # Draw player and enemies
    screen.blit(playerImg, (playerX, playerY))
    for i in range(num_of_enemies):
        screen.blit(enemyImg[i], (enemyX[i], enemyY[i]))
    
    pygame.display.update()