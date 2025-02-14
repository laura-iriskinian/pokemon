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

class Pokedex_menu(Menu):
    def __init__(self):
        super().__init__()

def Create_player():
    """Function to create a new player and assign basic pokedex"""
    

def menu_loop():
    pygame.init()
    run = True
    menu = Menu()
    second_menu=Second_menu()
    pokedex_menu = Pokedex_menu()
    current_menu = menu
    while run:
        #set the scene
        current_menu.draw_background()
        current_menu.draw_buttons()
        current_menu.select_menu_button()

        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #handle events based on the type of menu
            current_menu.handle_events(event)

            if event.type == KEYDOWN and event.key == K_RETURN:
                if current_menu == menu:
                    current_menu = second_menu
                else:
                    current_menu = menu
                
                # elif event.key == K_RETURN:
                    # if menu.selected_position == 1:
                    #     sign_in()
                    # if menu.selected_button == 2:
                    #     game()
                        

        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    menu_loop()