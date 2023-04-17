import pygame
from config import Config
import random

class LoadingScreen:
    def __init__(self):
        pygame.init()
        self.config = config = Config()
        self.screen = config.getScreen()
        self.width, self.height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        self.clock, self.logo = config.clock, config.logo
        self.background, self.fps = config.BLACK, config.FPS
        
        # Progress bar configuration
        self.progress_bar_length, self.progress_bar_thickness = 400, 20
        self.progress_bar_color_start = pygame.Color('#0062FF')
        self.progress_bar_color_end = pygame.Color('#FF6600')
        self.progress_bar_position = (self.width/2 - self.progress_bar_length/2, self.height - 150)
        self.progress = 0
        self.progress_load_finish = False
        self.time_since_last_pause = 0
        self.pause_duration = 0
        self.paused = False
        self.progress_bar_text = config.FONT_SMALL.render("Progression : {:.0%}".format(self.progress), True, config.WHITE, self.background)

    def show(self):
        start_screen = True
        progress_speed = 1/3  # 1/3 progress per second
        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Timer management last frame
            dt = self.clock.tick(self.fps) / 1000.0

            # Update progress bar
            if not self.paused:
                self.progress += dt * progress_speed
                if self.progress >= 1:
                    self.progress = 1
                    self.progress_load_finish = True
            else:
                self.time_since_last_pause += dt
                if self.time_since_last_pause >= self.pause_duration:
                    self.paused = False
                    self.time_since_last_pause = 0

            # Update progress bar text
            self.progress_bar_text = self.config.FONT_SMALL.render("Progression : {:.0%}".format(self.progress), True, self.config.WHITE)

            # Screen management
            self.screen.fill(self.background)

            # get the size of the screen
            screen_width, screen_height = self.screen.get_size()

            # Scale the logo to fit the screen
            logo_scale_factor = min(screen_width / self.logo.get_width(), screen_height / self.logo.get_height())
            scaled_logo = pygame.transform.rotozoom(self.logo, 0, logo_scale_factor)

            # Get the rect of the scaled logo
            logo_rect = scaled_logo.get_rect(center=(screen_width/2, screen_height/2))

            # Draw the scaled logo
            self.screen.blit(scaled_logo, logo_rect)

            # Draw the progress bar
            progress_bar_rect_bg = pygame.Rect(self.progress_bar_position[0], self.progress_bar_position[1], 
                                            self.progress_bar_length, self.progress_bar_thickness)
            pygame.draw.rect(self.screen, self.background, progress_bar_rect_bg)
            progress_bar_rect = pygame.Rect(self.progress_bar_position[0], self.progress_bar_position[1], 
                                            self.progress_bar_length*self.progress, self.progress_bar_thickness)
            mix_color = self.progress_bar_color_start.lerp(self.progress_bar_color_end, self.progress)
            pygame.draw.line(self.screen, mix_color, progress_bar_rect.topleft, progress_bar_rect.topright, self.progress_bar_thickness)

            # Draw the progress text
            progress_text_rect = self.progress_bar_text.get_rect(center=(screen_width/2, screen_height - 100))
            self.screen.blit(self.progress_bar_text, progress_text_rect)

            # Pause progress bar
            if self.progress < 1 and not self.paused:
                if random.random() < 0.01:  # pause with a 1% probability
                    self.paused = True
                    self.pause_duration = random.uniform(0.5, 1.5)  # pause for a random duration between 0.5 and 1.5 seconds

            pygame.display.flip()
