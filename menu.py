import pygame
from window import Window

class Button:
    def __init__(self, x, y, image, window):
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.window = window
    
    #draw button on the screen
    def draw_button(self):
        self.window.screen_menu.blit(self.image, (self.rect.x, self.rect.y))


class Menu():
    #first menus
    def __init__(self):

        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        
        #Load button images:
        self.sign_in_img = self.window.create_text_image("Sign in", self.window.text_font_menu, self.window.BLACK)
        self.new_player_img = self.window.create_text_image("New Player", self.window.text_font_menu, self.window.BLACK)
        
        #Create Button objects
        self.sign_in_button = Button(100,100,self.sign_in_img, self.window)
        self.new_player_button = Button(530,100,self.new_player_img, self.window)

    def draw_background(self):
        """function to draw background"""
        self.window.screen_menu.blit(self.background,(0,0))

    def draw_buttons(self):
        self.sign_in_button.draw_button()
        self.new_player_button.draw_button()

pygame.init()
run = True
menu = Menu()
while run:
    
    menu.draw_background()
    menu.draw_buttons()

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    pygame.display.update()


pygame.quit()


