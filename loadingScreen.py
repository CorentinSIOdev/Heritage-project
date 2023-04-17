import pygame
from config import Config


class LoadingScreen:
    def __init__(self):
        pygame.init()
        config = Config()
        self.screen = config.getScreen()
        self.width = config.SCREEN_WIDTH
        self.height = config.SCREEN_HEIGHT
        self.clock = config.clock
        self.blink_frequency = config.blink_frequency
        self.blink_on = config.blink_on
        self.blink_timer = config.blink_timer
        self.font_logo = config.FONT_LAUNCH_LOGO
        self.font_logo_color = config.RED
        self.font_text_launch = config.FONT_MEDIUM
        self.font_text_launch_color = config.RED
        self.background = config.BLACK
        self.fps = config.FPS
        

    def show(self):
        start_screen = True
        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start_screen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            # Timer management last frame
            dt = self.clock.tick(self.fps) / 1000.0
            
            # Updating the flashing timer
            self.blink_timer += dt

            # If the flashing time has expired, the flashing state is reversed and the timer is reset
            if self.blink_timer >= 1.0 / self.blink_frequency:
                self.blink_on = not self.blink_on
                self.blink_timer = 0
            
            # Screen management
            self.screen.fill(self.background)
            textLogo = self.font_logo.render("Heritage", True, self.font_logo_color)
            text_rect_logo = textLogo.get_rect(center=(self.width/2, self.height/2))
            self.screen.blit(textLogo, text_rect_logo)
            if self.blink_on:
                textLaunch = self.font_text_launch.render("Appuyer sur espace pour lancer", True, self.font_text_launch_color)
                text_rect_launch = textLaunch.get_rect(centerx=(self.width/2), bottom=self.height-150)
                self.screen.blit(textLaunch, text_rect_launch)
            
            pygame.display.flip()