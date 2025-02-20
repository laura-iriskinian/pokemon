import pygame
from pygame.locals import *
from models.window import Window
from models.button import Button
import json

with open("models/pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

# with open("models/pokedex.json", "r", encoding = "utf-8") as file:
#     player_pokedex = json.load(file)

class Player_menu():
    #first menu
    def __init__(self):

        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "player_menu"

        #Load button images:
        self.sign_in_img = self.window.create_text_image("Sign in", self.window.text_font_menu, self.window.BLACK)
        self.new_player_img = self.window.create_text_image("New Player", self.window.text_font_menu, self.window.BLACK)
        #Create Button objects
        self.sign_in_button = Button(100,100,self.sign_in_img, self.window)
        self.new_player_button = Button(530,100,self.new_player_img, self.window)
        #selection
        self.selected_position = 1
        self.buttons = (self.sign_in_button, self.new_player_button)
        self.total_buttons = len(self.buttons)

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))

    def draw_buttons(self):
        """method to draw button on screen"""
        self.sign_in_button.draw_button()
        self.new_player_button.draw_button()

    def select_menu_button(self):
        """method to show which button is selected"""

        for position, button in enumerate(self.buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)

    def start_player_menu(self):

        #set the scene
        self.draw_background()
        self.draw_buttons()
        self.select_menu_button()
        #handle events
        new_state = self.handle_events()
        return new_state
    
    def handle_events(self):   
        """method to handle menu events"""

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                
                if event.key == K_RIGHT:
                    self.selected_position = (self.selected_position % 2) +1 
                
                elif event.key == K_LEFT:
                    self.selected_position = (self.selected_position - 2) % self.total_buttons + 1 
                
                elif event.key == K_RETURN: 

                    if self.selected_position == 1 : # Sign in
                        return "connect_player" 
                        
                    elif self.selected_position == 2 : # New player
                        return "create_player"                   
                
        return "player_menu"