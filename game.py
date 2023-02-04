import pygame
import random

# initialize pygame and set up window
pygame.init()
window_size = (600, 800)
screen = pygame.display.set_mode(window_size)

# load player and enemy images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")

# initialize player and enemy positions
player_pos = [300, 700]
enemy_pos = [random.randint(0, 550), 0]

# initialize player and enemy speeds
player_speed = 5
enemy_speed = 5

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # move player based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    
    # move enemy downwards
    enemy_pos[1] += enemy_speed
    
    # redraw screen
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_pos)
    screen.blit(enemy_image, enemy_pos)
    pygame.display.update()

# quit pygame
pygame.quit()
