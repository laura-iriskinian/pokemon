import pygame
from pygame.locals import *
import json
import time
from models.window import Window
from models.button import Button
# from models.pokemon import Pokemon


# with open("models/pokemon.json", "r", encoding = "utf-8") as file:
#     data = json.load(file)

class Create_player_menu():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "create_player"

        #Player information
        self.request_player_name_img = self.window.create_text_image("Enter your name: ", self.window.text_font_menu, self.window.BLACK)
        self.request_player_name_button = Button(100,100, self.request_player_name_img, self.window)
        self.player_name = "" 
        self.input_box = pygame.Rect(100, 200, 300, 50) 
        self.typing = False
        self.error_msg_player_exists_img = self.window.create_text_image("This player already exists. \nType again or press ESC to go to previous menu", self.window.text_font_menu, self.window.BLACK)
        self.error_msg_player_exists_button = Button(100,280, self.error_msg_player_exists_img, self.window)
        self.player_added_img = self.window.create_text_image(f"New player created successfully!", self.window.text_font_menu, self.window.BLACK)
        self.player_added_button = Button(100,300, self.player_added_img, self.window)

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
            new_state = self.handle_events_create_player()
            pygame.display.update() 
        return new_state


    def handle_events_create_player(self):
        """method to handle events on the create player screen"""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    
                    self.current_state = "player_menu"
                    self.typing = False
                    return self.current_state
                
                elif event.key == K_RETURN:
                    if self.player_name and len(self.player_name) > 1:  
                        self.create_player()
                        return "starter_choice"
                    else: print("name too short")

                elif event.key == K_BACKSPACE:  
                    self.player_name = self.player_name[:-1]
                elif len(self.player_name) < 20: 
                    self.player_name += event.unicode

        return "create_player"      
            
    def create_player(self):
        """Function to create a new player and assign basic pokedex"""
        self.typing = False
        # load existing pokedex
        with open("models/pokedex.json", "r", encoding="utf-8") as file:
                pokedex = json.load(file)

        # check if player already exists in pokedex
        for player in pokedex["players"]:
            if player["player_name"] == self.player_name:
                # print(f"Player '{self.player_name}' already exists!")
                self.error_msg_player_exists_button.draw_button()
                pygame.display.update()
                time.sleep(3)
                self.player_name = "" 
                self.start_create_player()
            else: pass    

        # create new empty pokedex
        new_player = {
            "player_name": self.player_name, 'pokedex': [{'pokedex_id': 1, 'name': 'Bulbasaur', 'sprites': {'front': 'assets/pictures/Grass/bulbasaur_front.png'}, 'xp': 50}]}

        # add new player to pokedex
        pokedex["players"].append(new_player)

        # save new player to pokedex
        with open("models/pokedex.json", "w", encoding="utf-8") as file:
            json.dump(pokedex, file, indent=4, ensure_ascii=False)

        self.player_added_button.draw_button()
        pygame.display.update()
        time.sleep(2)
        self.player_name = ""
