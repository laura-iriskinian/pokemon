import pygame
from pygame.locals import *
from window import Window
from game_loop import *

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

        self.selected_position = 1 

    def draw_background(self):
        """function to draw background"""
        self.window.screen_menu.blit(self.background,(0,0))

    def draw_buttons(self):
        self.sign_in_button.draw_button()
        self.new_player_button.draw_button()

    #draw a rectangle around the currently selected button
    def draw_selected_button(self):
        if self.selected_position == 1:
            button_rect = self.sign_in_button.rect
        elif self.selected_position == 2:
            button_rect = self.new_player_button.rect

        pygame.draw.rect(self.window.screen, self.window.GREY, button_rect, 3)


pygame.init()
run = True
menu = Menu()
position = 1
while run:
    
    menu.draw_background()
    menu.draw_buttons()
    menu.draw_selected_button()

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
               menu.selected_position = 2 if menu.selected_position == 1 else 1
            
            elif event.key == K_RETURN:
                # if menu.selected_position == 1:
                #     sign_in()
                if menu.selected_button == 2:
                    game()
                    

    pygame.display.update()


pygame.quit()


