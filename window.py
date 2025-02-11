import pygame


class Window:
    def __init__(self):

        # color
        self.BLUE = (27, 1, 155)
        self.GREY = (128,128,128)

        # game window
        self.bottom_panel = 150
        self.screen_width = 800
        self.screen_height = 400 + self.bottom_panel

        pygame.display.set_caption("Pokemon") 
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
