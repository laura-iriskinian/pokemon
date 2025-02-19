import pygame
import pygame.draw_py
from pygame.locals import *
from models.button import Button
from models.window import Window

class Game_menu():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "game_menu"

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

        # button for game_menu
        self.buttons = (self.resume_game_button, self.pokedex_button, self.add_pokemon_button, self.new_game_button)
        self.total_buttons = len(self.buttons)


    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))


    def draw_buttons(self):
        self.resume_game_button.draw_button()
        self.pokedex_button.draw_button()
        self.add_pokemon_button.draw_button()
        self.new_game_button.draw_button()

    #Draw a rectangle around the selected button
    def select_menu_button(self):
        for position, button in enumerate(self.buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)


    def handle_events_game_menu(self):   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #handle events based on the type of menu

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.selected_position = (self.selected_position % self.total_buttons) +1  
                if event.key == K_UP:
                    self.selected_position = (self.selected_position - 2) % self.total_buttons + 1

                if event.key == K_ESCAPE:
                    return "player_menu"

                if event.key == K_RETURN:
                    if self.selected_position == 1 :
                        return "fight"  
                    if self.selected_position == 3:
                        return "add_pokemon"
                    else:
                        return "game_menu"


        return "game_menu"


    def start_game_menu(self):

        #set the scene
        self.draw_background()
        self.draw_buttons()
        self.select_menu_button()

        #handle events

        new_state = self.handle_events_game_menu()
        return new_state


