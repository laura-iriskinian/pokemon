import pygame
from pygame.locals import *
from models.button import Button
from models.menu import Menu
from models.window import Window

class Second_menu(Menu):
    def __init__(self):
        super().__init__()

        #Load button images:
        self.resume_game_img = self.window.create_text_image("Resume game", self.window.text_font_menu, self.window.BLACK)
        self.pokedex_img = self.window.create_text_image("Pokedex", self.window.text_font_menu, self.window.BLACK)
        self.add_pokemon_img = self.window.create_text_image("Add pokemon", self.window.text_font_menu, self.window.BLACK)
        self.new_game_img = self.window.create_text_image("New game", self.window.text_font_menu, self.window.BLACK)

        #Create Button objects
        self.resume_game_button = Button(100,100,self.resume_game_img, self.window)
        self.pokedex_button = Button(100,150,self.pokedex_img, self.window)
        self.add_pokemon_button = Button(100,200,self.add_pokemon_img, self.window)
        self.new_game_button = Button(100,250,self.new_game_img, self.window)

    def draw_buttons(self):
        self.resume_game_button.draw_button()
        self.pokedex_button.draw_button()
        self.add_pokemon_button.draw_button()
        self.new_game_button.draw_button()

    #Draw a rectangle around the selected button
    def select_menu_button(self):
        buttons = (self.resume_game_button, self.pokedex_button, self.add_pokemon_button, self.new_game_button)
        for position, button in enumerate(buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)
    
    def handle_events(self, event):   
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.selected_position = (self.selected_position % 4) +1  
