from window import Window
import pygame

class Fight():
    """class to print combat"""

    def __init__(self):
        # background image
        self.window = Window() 
        self.background = pygame.image.load("assets/pictures/background.png").convert_alpha()

    def draw_panel(self):
        """draw rectangle for bottom panel"""
        # full Rectangle 
        rectangle_left = pygame.Rect(0, self.window.screen_height - self.window.bottom_panel, self.window.screen_width / 2, self.window.bottom_panel)
        pygame.draw.rect(self.window.screen, self.window.BLUE, rectangle_left)
        rectangle_right = pygame.Rect(self.window.screen_width/2, self.window.screen_height - self.window.bottom_panel, self.window.screen_width / 2, self.window.bottom_panel)
        pygame.draw.rect(self.window.screen, self.window.BLUE, rectangle_right)

        # outline rectangle 
        pygame.draw.rect(self.window.screen, self.window.GREY, rectangle_left, 3)
        pygame.draw.rect(self.window.screen, self.window.GREY, rectangle_right, 3)

    def draw_background(self):
        """function to drawing background"""
        self.window.screen.blit(self.background,(0,0))