import pygame
from pygame.locals import *
import json
from models.window import Window
from models.button import Button
# from models.pokemon import Pokemon


# with open("models/pokemon.json", "r", encoding = "utf-8") as file:
#     data = json.load(file)

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    pokedex = json.load(file)

class Connect_player():
    def __init__(self):
        #background
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.rect_width = self.window.screen_width - 100
        self.rect_height = self.window.screen_height - 100
        self.background_select_player = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        #buttons 
        self.select_player_img = self.window.create_text_image("Select your player :", self.window.text_font_menu, self.window.BLACK)
        self.select_pokemon_img = self.window.create_text_image("Select your pokemon", self.window.text_font_menu, self.window.WHITE)
        #Create Button objects
        self.select_player_button = Button(300,100,self.select_player_img, self.window)
        self.select_pokemon_button = Button(300,100,self.select_pokemon_img, self.window)
        #selection
        self.buttons = (self.select_player_button, self.select_pokemon_button)
        self.total_buttons = len(self.buttons)
        self.selected_position = 1
        self.current_state = "connect_player"
        self.select = False

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))

    def draw_player_choice(self):
        with open("models/pokedex.json", "r", encoding = "utf-8") as file:
            pokedex = json.load(file)


    def draw_background_select_pokemon(self):
        self.background_select_player = pygame.Rect(60,70,self.window.screen_width-110,self.window.screen_height-110)
        pygame.draw.rect(self.window.screen,self.window.BLUE,self.background_select_player)
        pygame.draw.rect(self.window.screen,self.window.GREY,self.background_select_player,4)

    def connect_player(self):
        self.select = True
        while self.select:
            #set the scene
            self.draw_background() 
            self.select_player_button.draw_button()
            self.draw_background_select_pokemon()      
            #handle events 
            self.handle_events_connect_player()
            pygame.display.update() 
        return "game_menu"    
                      

    def handle_events_connect_player(self):
        """method to handle events on the connect player screen"""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("ok")
                    return "player_menu"           
  
        return "connect_player"      
            
    