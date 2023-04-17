import pygame

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    pygame.display.update()
    
# Quit pygame
pygame.quit()