import pygame


class Config:
    def __init__(self):
        # Pygame Configuration
        pygame.init()

        # Screen Configuration
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        self.setScreen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption("Heritage")

        # Color Configuration
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Font Configuration
        self.FONT_SMALL = pygame.font.Font(None, 24)
        self.FONT_MEDIUM = pygame.font.Font(None, 36)
        self.FONT_LARGE = pygame.font.Font(None, 48)

        # Clock Configuration
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Image Configuration
        self.logo = pygame.image.load("assets/images/logo/heritage.png")

    def getCaption(self):
        return self.caption

    def getScreen(self):
        return self.setScreen