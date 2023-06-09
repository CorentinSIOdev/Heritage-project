import pygame
from config import Config
from loadingScreen import LoadingScreen

# Initialize pygame
pygame.init()

config = Config()

# Set the screen
screen = config.getScreen()
config.getCaption()

# Initialize the loading screen
loading_screen = LoadingScreen()

# Game Loop
running = True
loading = True
while running:
    # Event management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Show the loading screen
    if loading:
        loading_screen.show()
        loading = False

    # Game logic
    # ...

    # Screen management
    if loading_screen.progess_load_finish == True:
        config.setScreen.fill((255, 255, 255))

    # ...

    # Screen update
    pygame.display.update()

    # Timer management last frame
    config.clock.tick(config.FPS)

# Fermeture de Pygame
pygame.quit()
