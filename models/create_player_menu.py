import pygame
from pygame.locals import *
from models.window import Window
from models.button import Button
# from models.pokemon import Pokemon
import json

with open("models/pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    player_pokedex = json.load(file)

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
        #set the scene
        self.typing = True
        self.draw_background()
        self.request_player_name_button.draw_button()
        self.draw_text_input()
        # pygame.draw.rect(self.window.screen, self.window.WHITE, self.input_box, 2)
        # self.window.draw_text(self.player_name, self.window.text_font_menu, self.window.BLACK, 110, 210)
    
        #handle events
        new_state = self.handle_events_create_player()
        pygame.display.update()
        return new_state

    def handle_events_create_player(self):
        """method to handle events on the create player screen"""
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                print("ok")
                if event.key == K_ESCAPE:
                    self.current_state = "player_menu"
                
                elif event.key == K_RETURN:
                    if len(self.player_name) < 12:  
                        self.player_name += event.unicode
                    self.create_player()
                    self.typing = False
                    return "game_menu"
                
                elif event.key == K_BACKSPACE:  
                    self.player_name = self.player_name[:-1]
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    player_input += chr(event.key)
                
            
    def create_player(self):
        """Function to create a new player and assign basic pokedex"""
            # get player name
        self.player_name = input("").strip()
        if not self.player_name.strip():
            print("You must enter a name")
            return

        # load existing pokedex
        with open("models/pokedex.json", "r", encoding="utf-8") as file:
                player_pokedex = json.load(file)

        # check if player already exists in pokedex
        for player in player_pokedex:
            if player["player_name"] == self.player_name:
                print(f"Player '{self.player_name}' already exists!")
                return

        # create new empty pokedex
        new_player = {
            "player_name": self.player_name,
            "pokedex": [] 
        }

        # add new player to pokedex
        player_pokedex.append(new_player)

        # save new player to pokedex
        with open("models/pokedex.json", "w", encoding="utf-8") as file:
            json.dump(player_pokedex, file, indent=4, ensure_ascii=False)

        print(f"Player '{self.player_name}' has been created successfully!")
        self.time.wait(2)

        return "game_menu"