import pygame
from config import Config
import random

class LoadingScreen:
    def __init__(self):
        # Pygame Configuration
        pygame.init()

        # Screen Configuration
        self.config = config = Config()
        self.screen = config.getScreen()
        self.width, self.height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
        self.clock, self.logo = config.clock, config.logo
        self.fps = config.FPS
        
        # Progress bar configuration
        self.progress_bar_length, self.progress_bar_thickness = 250, 10
        self.progress_bar_position = (self.width/2 - self.progress_bar_length/2, self.height - 150)
        self.progress = 0
        self.progress_load_finish = False
        self.time_since_last_pause = 0
        self.pause_duration = 0
        self.paused = False
        self.border_color = config.WHITE
        self.border_radius = 5
        self.progress_bar_radius = 2
        self.border_width = 2
        self.progress_color_start = pygame.Color("#32374d")
        self.progress_color_end = pygame.Color("#c35e26")

        # Background configuration
        self.background_gif = pygame.image.load("assets/images/background_loading/background.gif")
        self.background = pygame.transform.scale(self.background_gif, (self.width, self.height))


    def show(self):
        start_screen = True
        progress_speed = 1/5  # 1/5 progress per second
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
            if self.progress <= 0.0:
                self.progress_bar_text = self.config.FONT_SMALL.render("Début de la mise à jour", True, self.config.WHITE)
            elif self.progress_load_finish:
                self.progress_bar_text = self.config.FONT_SMALL.render("Mise à jour terminée !", True, self.config.WHITE)
            else:
                self.progress_bar_text = self.config.FONT_SMALL.render("Mise à jour : {:.0%}".format(self.progress), True, self.config.WHITE)

            # Get background image
            self.screen.blit(self.background, (0, 0))

            # Get the size of the screen
            screen_width, screen_height = self.screen.get_size()

            # Scale the logo to fit the screen
            logo_scale_factor = min(screen_width / self.logo.get_width(), screen_height / self.logo.get_height())
            scaled_logo = pygame.transform.rotozoom(self.logo, 0, logo_scale_factor)

            # Get the rect of the scaled logo
            logo_rect = scaled_logo.get_rect(center=(screen_width/2, screen_height/2))

            # Draw the scaled logo
            self.screen.blit(scaled_logo, logo_rect)

            # Draw the progress bar
            border_rect = pygame.Rect(self.progress_bar_position[0]-self.border_width, self.progress_bar_position[1]-self.border_width, 
                                        self.progress_bar_length+2*self.border_width, self.progress_bar_thickness+2*self.border_width)
            pygame.draw.rect(self.screen, self.border_color, border_rect, border_radius=self.border_radius, width=0)
            pygame.draw.rect(self.screen, self.border_color, pygame.Rect(self.progress_bar_position[0], self.progress_bar_position[1], 
                                        self.progress_bar_length, self.progress_bar_thickness))



            # Calculer la position et la taille de la barre de progression
            progress_bar_rect = pygame.Rect(self.progress_bar_position[0], self.progress_bar_position[1], 
                                            self.progress_bar_length*self.progress, self.progress_bar_thickness)

            # Dessiner la barre de progression avec les deux couleurs vives
            if self.progress_load_finish:
                progress_color = self.progress_color_end
            else:
                progress_color = ((1 - self.progress) * self.progress_color_start[0] + self.progress * self.progress_color_end[0],
                                (1 - self.progress) * self.progress_color_start[1] + self.progress * self.progress_color_end[1],
                                (1 - self.progress) * self.progress_color_start[2] + self.progress * self.progress_color_end[2])
            pygame.draw.rect(self.screen, progress_color, progress_bar_rect, border_radius=self.progress_bar_radius, width=0)


            # Draw the progress text
            progress_text_rect = self.progress_bar_text.get_rect(center=(screen_width/2, screen_height - 100))
            self.screen.blit(self.progress_bar_text, progress_text_rect)

            # Pause progress bar
            if self.progress < 1 and not self.paused:
                if random.random() < 0.01:  # pause with a 1% probability
                    self.paused = True
                    self.pause_duration = random.uniform(0.5, 1.5)  # pause for a random duration between 0.5 and 1.5 seconds

            pygame.display.flip()

