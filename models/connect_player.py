import pygame
from pygame.locals import *
import json
import time
from models.window import Window
from models.button import Button
# from models.pokemon import Pokemon


# with open("models/pokemon.json", "r", encoding = "utf-8") as file:
#     data = json.load(file)

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    pokedex = json.load(file)

class Create_player_menu():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "create player"

        #Player information
        self.request_player_name_img = self.window.create_text_image("Enter your name: ", self.window.text_font_menu, self.window.BLACK)
        self.request_player_name_button = Button(100,100, self.request_player_name_img, self.window)
        self.player_name = "" 
        self.input_box = pygame.Rect(100, 200, 300, 50) 
        self.typing = False

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))

    def draw_text_input(self):
        """Method to show the input text"""
        pygame.draw.rect(self.window.screen, self.window.WHITE, self.input_box, 2)
        self.window.draw_text(self.player_name, self.window.text_font_menu, self.window.BLACK, 110, 210)
        
    def start_create_player(self):
        self.typing = True
        while self.typing:
            #set the scene
            self.draw_background()
            self.request_player_name_button.draw_button()
            self.draw_text_input()        
            #handle events 
            self.handle_events_create_player()
            pygame.display.update() 
        return "game_menu"    
                      

    def handle_events_create_player(self):
        """method to handle events on the create player screen"""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.typing = False
                    self.current_state = "player_menu"
                
                elif event.key == K_RETURN:
                    if self.player_name and len(self.player_name) > 1:  
                        self.create_player()
                    else: print("name too short")

                elif event.key == K_BACKSPACE:  
                    self.player_name = self.player_name[:-1]
                elif len(self.player_name) < 20: 
                    self.player_name += event.unicode
                  
        return "game_menu"      
            
    def create_player(self):
        """Function to create a new player and assign basic pokedex"""
        self.typing = False
        # load existing pokedex
        with open("models/pokedex.json", "r", encoding="utf-8") as file:
                pokedex = json.load(file)

        # check if player already exists in pokedex
        for player in pokedex:
            if player["player_name"] == self.player_name:
                print(f"Player '{self.player_name}' already exists!")
                return

        # create new empty pokedex
        new_player = {
            "player_name": self.player_name, 'pokedex': [{'pokedex_id': 1, 'name': 'Bulbasaur', 'sprites': {'front': 'assets/pictures/Grass/bulbasaur_front.png'}, 'xp': 50}]}

        # add new player to pokedex
        pokedex.append(new_player)

        # save new player to pokedex
        with open("models/pokedex.json", "w", encoding="utf-8") as file:
            json.dump(pokedex, file, indent=4, ensure_ascii=False)

        print(f"Player '{self.player_name}' has been created successfully!")
