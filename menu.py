import pygame
from pygame.locals import *
from window import Window
from game_loop import *
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

    #Draw a rectangle around the selected button
    def select_menu_button(self):
        buttons = (self.resume_game_button, self.pokedex_button, self.add_pokemon_button, self.new_game_button)
        for position, button in enumerate(buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)


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
            
            # elif event.key == K_RETURN:
                # if menu.selected_position == 1:
                #     sign_in()
                # if menu.selected_button == 2:
                #     game()
                    

    pygame.display.update()


pygame.quit()

