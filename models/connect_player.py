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
        self.selected_position = 1
        self.current_state = "connect_player"

        #button to select player
        self.button_select_player = []
        self.player_list = self.get_player_list()
        self.total_buttons_select_player = len(self.player_list) + 1
        self.position_player = self.get_position_player()
        self.selected_position_select_player = 0

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))
        self.window.draw_text("Select player:",self.window.text_font_menu,self.window.BLACK,300,20) 

    def get_player_list(self):
        self.player_list = []
        for self.player_name in pokedex["players"]:
            self.player_list.append(self.player_name["player_name"])
        return self.player_list
    
    def get_position_player(self):
        self.position_player = []
        for position, player in enumerate(self.player_list):
            self.position_player.append(position)
        return self.position_player

    def draw_player_list(self):
        #column1
        position_x = 60
        position_y = 90
        for self.player_name in self.player_list:
            self.player_name_img = self.window.create_text_image(self.player_name, self.window.text_font_battle, self.window.BLACK)
            self.player_name_button = Button(position_x, (position_y + position_y), self.player_name_img, self.window)
            self.player_name_button.window.screen.blit(self.player_name_img, (position_x, (position_y + 10)))
            position_y += 40
        return self.button_select_player    

    def select_player_name(self):
        for position, self.player_name_button in enumerate(self.button_select_player):
            if position == self.selected_position_select_player:
                pygame.draw.rect(self.window.screen, self.window.WHITE, self.player_name_img, 4)


    def connect_player(self):
        #set the scene
        self.draw_background() 
        self.draw_player_list() 
        self.select_player_name()  
        #handle events 
        new_state = self.handle_events_connect_player()
        return new_state    
                      

    def handle_events_connect_player(self):
        """method to handle events on the connect player screen"""
        for i, self.player_name in pokedex["players"]:
            return i
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "player_menu"  
                
                if event.key == K_DOWN:
                    self.selected_position_select_player = (self.selected_position % i) +1 
                
                elif event.key == K_UP:
                    self.selected_position = (self.selected_position - i) % self.total_buttons_select_player + 1            
  
        return "connect_player"      
            
    