

import pygame
import random

pygame.init()


# Setting up the window

WIDTH, HEIGHT = 200, 200
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Lets Play")

# COLORS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = ("teal")

#LOADS images at start

dice_images = {}
for i in range(1,7):
    image = pygame.image.load(f"dice_images/side{i}.png")
    #scale
    dice_images[i] = pygame.transform.scale(image, (100, 100))

#CLOCK for FPS
clock = pygame.time.Clock()

def draw_die_face(face_number):
    """This will draw die with my PNG"""
    die_size = 200
    x = (WIDTH - die_size) // 2
    y = (HEIGHT - die_size) //2

    # Draw the die square (background)
    pygame.draw.rect(screen, RED, (x, y, die_size, die_size))
    pygame.draw.rect(screen, BLACK, (x, y, die_size, die_size), 3)  # Border

    # Draw the image centered on the die
    image = dice_images[face_number]
    image_x = x + (die_size - image.get_width()) // 2
    image_y = y + (die_size - image.get_height()) // 2
    screen.blit(image, (image_x, image_y))


# Start with face 1
current_face = 1
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_face = random.randint(1, 6)

    screen.fill(WHITE)
    draw_die_face(current_face)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


