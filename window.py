import pygame


class Window:
    """class to define the window, to link : window.screen"""
    def __init__(self):

        # color
        self.BLUE = (27, 1, 155)
        self.GREY = (128,128,128)
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)

        # text font 
        self.text_font_menu_battle = pygame.font.SysFont("Arial",30)
        self.text_font_menu = pygame.font.SysFont("Arial", 25, bold=True)        
        self.text_font_hp_opponent = pygame.font.SysFont("Arial",20,bold=True)


        # game window
        self.bottom_panel = 150
        self.screen_width = 800
        self.screen_height = 400 + self.bottom_panel
        self.screen_height_total = 550

        # position y button game pannel
        self.py_rectangle_top = (self.screen_height - self.bottom_panel)+3
        self.py_rectangle_middle = (self.screen_height - (self.bottom_panel - (self.bottom_panel/3)))
        self.py_rectangle_bottom = (self.screen_height - (self.bottom_panel/3))

        # position x button game panel
        self.px_pannel_left = 3
        self.px_pannel_right = (self.screen_width/2)+3

        # size button x/y button game pannel
        self.sy_button = (self.bottom_panel/3)-3
        self.sx_button = (self.screen_width / 2)-6

        pygame.display.set_caption("Pokemon") 
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_menu = pygame.display.set_mode((self.screen_width, self.screen_height_total))

    def draw_text(self,text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        self.screen.blit(img,(x,y))

    #create a surface with the text image
    def create_text_image(self, text, font, text_col):
        return font.render(text, True, text_col)