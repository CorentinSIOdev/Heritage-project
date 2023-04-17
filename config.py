import pygame


class Config:
    def __init__(self):
        # Pygame Configuration
        pygame.init()

        # Screen Configuration
        self.infoObject = pygame.display.Info()
        self.SCREEN_WIDTH = self.infoObject.current_w
        self.SCREEN_HEIGHT = self.infoObject.current_h
        self.setScreen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption("Heritage")

        # Color Configuration
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Font Configuration
        self.FONT_LAUNCH_LOGO = pygame.font.Font(None, 64)
        self.FONT_SMALL = pygame.font.Font(None, 24)
        self.FONT_MEDIUM = pygame.font.Font(None, 36)
        self.FONT_LARGE = pygame.font.Font(None, 48)

        # Clock Configuration
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Event Configuration
        self.CUSTOM_EVENT_1 = pygame.USEREVENT + 1
        self.CUSTOM_EVENT_2 = pygame.USEREVENT + 2

        # Animation Configuration
        # Flashes Configuration
        self.blink_frequency = 2.5  # number of flashes per second
        self.blink_on_time = 0.5  # time in seconds that the text is visible

        # Game Configuration
        self.blink_on = True
        self.blink_timer = 0

    def getCaption(self):
        return self.caption

    def getScreen(self):
        return self.setScreen