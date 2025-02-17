import pygame
from pygame.locals import *
from models.window import Window
from models.button import Button

class Player_menu():
    #first menu
    def __init__(self):

        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.run = True
        self.current_state = ""
        
        #Load button images:
        self.sign_in_img = self.window.create_text_image("Sign in", self.window.text_font_menu, self.window.BLACK)
        self.new_player_img = self.window.create_text_image("New Player", self.window.text_font_menu, self.window.BLACK)
        
        #Create Button objects
        self.sign_in_button = Button(100,100,self.sign_in_img, self.window)
        self.new_player_button = Button(530,100,self.new_player_img, self.window)

        #Player information
        self.request_player_name_img = self.window.create_text_image("Enter your name: ", self.window.text_font_menu, self.window.BLACK)
        self.request_player_name_button = Button(100,100, self.request_player_name_img, self.window)
        self.player_name = ""

    def draw_background(self):
        """method to draw background"""
        self.window.screen_menu.blit(self.background,(0,0))

    def draw_buttons(self):
        """method to draw button on screen"""
        self.sign_in_button.draw_button()
        self.new_player_button.draw_button()

    def select_menu_button(self):
        """method to show which button is selected"""
        buttons = (self.sign_in_button, self.new_player_button)
        for position, button in enumerate(buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)

    def handle_events(self, event):   
        """method to handle menu events"""
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.selected_position = (self.selected_position % 2) +1 
        pygame.display.update()
                

    def start_player_menu(self):

        while self.run:

            #set the scene
            self.draw_background()
            self.draw_buttons()
            self.select_menu_button()

            #handle events
            for event in pygame.event.get():
                self.handle_events(event)

                if event.type == KEYDOWN and event.key == K_RETURN:
                    if self.selected_position == 1 :
                        self.current_state = "game_menu"
                        return self.current_state
                    else:
                        self.current_state = "player_menu"
                        return self.current_state
                


            pygame.display.update()

        pygame.quit()


def Create_player(self):
    """Function to create a new player and assign basic pokedex"""
    self.draw_background()
    self.request_player_name_button.draw_button()


