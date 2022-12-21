import pygame
import random

#set up pygame
pygame.init()

#set up the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set up the clock
clock = pygame.time.Clock()

#Set up the player
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 50
player_speed = 5

#Set up the shapes
shape_size = 50
shape_speed = 5
shapes = []

#Set up the colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

#Set up the score
score = 0

#Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    #keep the player on the screen
    player_x = max(0, min(player_x, SCREEN_WIDTH - 50))

    #move the shapes
    for shape in shapes:
        shape.move()

    # Remove shapes that have fallen off the bottom of the screen
    shapes = [shape for shape in shapes if shape.y < SCREEN_HEIGHT]

    # Add new shapes at random intervals
    if random.randint(0, 100) == 0:
        x = random.randint(0, SCREEN_WIDTH - shape_size)
        y = 0
        color = random.choice(colors)
        shape = rect(x, y, shape_size, shape_size, shape_speed, color)
        shapes.append(shape)

    # Check for collisions
    for shape in shapes:
        if shape.collides_with(player_x, player_y, 50, 50):
            score -= 1
            shape.reset()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, 50, 50))

    for shape in shapes:
        shape.draw(screen)
    pygame.display.set_caption("Shape Shooter | Score: {}".format(score))
    pygame.display.flip()

    #Update the clock
    clock.tick(60)

# Quit pygame
pygame.quit()

