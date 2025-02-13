import pygame
from pygame.locals import *
from window import Window
from button import Button

class Menu:
    #first menu
    def __init__(self):

        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        
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

    #draw a rectangle around the currently selected button
    def select_menu_button(self):
        buttons = (self.sign_in_button, self.new_player_button)
        for position, button in enumerate(buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)
    
    
class Second_menu(Menu):
    def __init__(self):
        super().__init__(self)

#          #Load button images:
        self.resume_game_img = self.window.create_text_image("Resume game", self.window.text_font_menu, self.window.BLACK)
        self.pokedex_img = self.window.create_text_image("Pokedex", self.window.text_font_menu, self.window.BLACK)
        self.add_pokemon_img = self.window.create_text_image("Add pokemon", self.window.text_font_menu, self.window.BLACK)
        self.new_game_img = self.window.create_text_image("New game", self.window.text_font_menu, self.window.BLACK)

#         #Create Button objects
        self.resume_game_button = Button(530,100,self.resume_game_img, self.window)
        self.pokedex_button = Button(530,100,self.pokedex_img, self.window)
        self.add_pokemon_button = Button(530,100,self.add_pokemon_img, self.window)
        self.new_game_button = Button(100,100,self.new_game_img, self.window)

    def draw_buttons(self):
        self.resume_game_button.draw_button()
        self.pokedex_button.draw_button()
        self.add_pokemon_button.draw_button()
        self.new_game_button.draw_button()

    #draw a rectangle around the currently selected button
    def select_menu_button(self):
        buttons = (self.resume_game_button, self.pokedex_button, self.add_pokemon_button, self.new_game_button)
        for position, button in enumerate(buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)

class Add_player_menu(Menu):
        def __init__(self):
            super().__init__
            self.input_img = self.window.create_text_image("Please enter your name", self.window.text_font_menu, self.window.BLACK)
            self.input_button = Button((self.window.screen_width / 2) - 100, self.window.screen_height_total / 2, self.sign_in_img, self.window)
            self.player_input = ""

        def draw_buttons(self):
            self.input_button.draw_button()

        # def add_player(self):
        #     self.player_input = ""

        def display_input(self):
            self.player_input = self.window.draw_text(self.player_input, self.window.text_font_menu, self.window.BLACK, 330, 300)
            return self.player_input
            
        

pygame.init()

run = True

menu = Menu()

while run:
    
    menu.draw_background()
    menu.draw_buttons()
    menu.select_menu_button()

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                menu.selected_position = 2 if menu.selected_position == 1 else 1
            
            elif event.key == K_RETURN:
                
                if menu.selected_position == 1:
                    #sign_in with existing player
                    sign_in()
                elif menu.selected_position == 2:
                    game_loop()
                    super.draw_background()
                    Add_player_menu.draw_buttons()
                    menu.display_input()
                
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()

                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                # game.gamestate = "menu"
                                menu()

                            elif event.key == K_RETURN:
                                if player_input and len(player_input) > 1:
                                    player_input = player_input

                            elif event.key == K_BACKSPACE:
                                player_input = player_input[:-1]

                            elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                                player_input += chr(event.key)

                
                    

    pygame.display.update()


pygame.quit()


    