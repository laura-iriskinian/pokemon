import pygame
from pygame.locals import *
import json
from models.window import Window
# from models.button import Button
# from models.pokemon import Pokemon


# with open("models/pokemon.json", "r", encoding = "utf-8") as file:
#     data = json.load(file)

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    pokedex = json.load(file)

class Connect_player():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "connect_player"
        self.select = False

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))
        
    def connect_player(self):
        self.select = True
        while self.select:
            #set the scene
            self.draw_background()       
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
            
    