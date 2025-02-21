from models.window import Window
from models.pokemon import Pokemon
from models.button import Button
from models.connect_player import Connect_player


import json
import random
import pygame
from pygame.locals import *

with open("models/pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)


class Fight():
    """class to print combat"""
    def __init__(self,player_name):

        # background image
        self.window = Window() 
        self.background = pygame.image.load("assets/pictures/background.png").convert_alpha()
        self.connect_player = Connect_player()

        # create button objects
        self.attack_button = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_top, self.window.sx_button, self.window.sy_button)
        self.run_button = pygame.Rect(self.window.px_pannel_left,self.window.py_rectangle_middle,self.window.sx_button,self.window.sy_button)
        self.change_pokemon_button = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_bottom,self.window.sx_button,self.window.sy_button)
        
        self.buttons = (self.attack_button,self.run_button,self.change_pokemon_button)
        self.total_buttons = len(self.buttons)

        self.selected_position = 1

        # pokemon object
        self.player_name = player_name
        self.pokemon_player_selected = self.get_pokemon_player_selected()
        self.pokemon_player = Pokemon(self.pokemon_player_selected)
        self.pokemon_opponent_id = self.get_pokemon_opponent_id()
        self.pokemon_opponent = [Pokemon(self.pokemon_opponent_id)]

    def get_pokemon_player_selected(self):

        with open("models/pokedex.json", "r", encoding = "utf-8") as file:
            pokedex_data = json.load(file)

        print(f"player name = {self.player_name}")

        for player in pokedex_data["players"]:
            if player["player_name"] == self.player_name:
                    for pokemon in player["pokedex"]:
                        if pokemon["selected"] == True:
                            pokemon_id_player = pokemon["pokemon_id"]

        return pokemon_id_player

    def add_to_pokedex(self):

        with open("models/pokedex.json", "r", encoding = "utf-8") as file:
            pokedex_data = json.load(file)

        new_pokemon = {
        "pokemon_id" : self.pokemon_opponent[0].pokemon_id,
        "name" : self.pokemon_opponent[0].pokemon_name,
        "sprite" : self.pokemon_opponent[0].get_pokemon_sprite(),
        "xp" : 0,
        "selected": False
    }
    
        for player in pokedex_data["players"]:
            if player["player_name"] == self.player_name:
                
                if not isinstance(player["pokedex"], list):
                    player["pokedex"] = [player["pokedex"]]
                
                if new_pokemon not in player["pokedex"]:
                    player["pokedex"].append(new_pokemon)
                else:
                    print(f"Pokemon déjà présent dans le pokédex")

        with open("models/pokedex.json", "w", encoding="utf-8") as file:
            json.dump(pokedex_data, file, ensure_ascii=False, indent=4)


    def get_pokemon_opponent_id(self):

        with open("models/pokemon.json", "r", encoding = "utf-8") as file:
            data = json.load(file)

        available_ids = []
        for pokemon in data["pokemon"]:
                if pokemon["active"] == True:
                    available_ids.append(pokemon["pokedex_id"])
        return random.choice(available_ids)

    def initialize_opponent(self):

        self.pokemon_opponent.clear()

        new_pokemon_opponent_id = self.get_pokemon_opponent_id()

        return self.pokemon_opponent.append(Pokemon(new_pokemon_opponent_id))
        

    def draw_panel(self):
        """draw rectangle for bottom panel"""
        # full Rectangle 
        rectangle_left = pygame.Rect(0, self.window.screen_height - self.window.bottom_panel, self.window.screen_width / 2, self.window.bottom_panel)
        pygame.draw.rect(self.window.screen, self.window.BLUE, rectangle_left)
        rectangle_right = pygame.Rect(self.window.screen_width/2, self.window.screen_height - self.window.bottom_panel, self.window.screen_width / 2, self.window.bottom_panel)
        pygame.draw.rect(self.window.screen, self.window.BLUE, rectangle_right)

        # outline rectangle 
        pygame.draw.rect(self.window.screen, self.window.GREY, rectangle_left, 3)
        pygame.draw.rect(self.window.screen, self.window.GREY, rectangle_right, 3)

        self.window.draw_text("Attack !",self.window.text_font_menu_battle,self.window.WHITE,50, (self.window.screen_height - self.window.bottom_panel)+6)
        self.window.draw_text("Run ",self.window.text_font_menu_battle,self.window.WHITE,50, (self.window.screen_height - (self.window.bottom_panel - (self.window.bottom_panel/3))))
        self.window.draw_text("Change pokemon",self.window.text_font_menu_battle,self.window.WHITE,50, (self.window.screen_height - (self.window.bottom_panel/3)))

    def draw_background_fight(self):
        """function to drawing background"""
        self.window.screen.blit(self.background,(0,0))

    def select_menu_button_battle(self):
        """method to show which button is selected"""

        for position, button in enumerate(self.buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button, 3)
        

    def handle_events_battle(self):   
        """method to handle menu battle events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.selected_position = (self.selected_position % self.total_buttons) +1  
                if event.key == K_UP:
                    self.selected_position = (self.selected_position - 2) % self.total_buttons + 1

                if event.key == K_RETURN:
                    if self.selected_position == 1 :
                        self.trainer_attack()
                    if self.selected_position == 2 :
                        if random.random() > 0.1:
                            return "game_menu"
                        else:
                            self.pokemon_opponent[0].attack(self.pokemon_player,"opponent")
                            pygame.time.delay(500)
                    else:
                        return "fight"
                    
        return "fight"

    def trainer_attack(self):
        """link with handle_events_battle = player attack and opponent attack"""


        # player attack 
        self.pokemon_player.attack(self.pokemon_opponent[0],"player")

        # if pokemon life opponnent = 0 -> replace a pokemon oponant
        if self.pokemon_opponent[0].pokemon_life <=0:
            self.pokemon_player.win_battle()
            self.add_to_pokedex()
            del self.pokemon_opponent[0]
            self.pokemon_opponent.append(Pokemon(self.pokemon_opponent_id))

        

        # opponent attack
        self.pokemon_opponent[0].attack(self.pokemon_player,"opponent")

        if self.pokemon_player.pokemon_life <= 0:
            self.pokemon_player.pokemon_life = self.pokemon_player.get_pokemon_hp()
            return "lose_game"

        pygame.time.delay(500)
        pygame.display.update()

        # reset background
        self.draw_background_fight()

        # # draw pokemons 
        self.pokemon_player.draw_pokemon_player(self.pokemon_player)
        self.pokemon_opponent[0].draw_pokemon_opponent(self.pokemon_opponent[0])
        
        # panel 
        self.draw_panel()

        # text lifes
        self.pokemon_opponent[0].draw_pokemon_opponent_hp(self.pokemon_opponent[0])
        self.pokemon_player.draw_pokemon_player_hp(self.pokemon_player)

        return "fight"
    
    def draw_xp_bar(self):
        bar_rect = pygame.Rect(160, 160, 200, 10)
        pygame.draw.rect(self.window.screen, self.window.BLACK, bar_rect, 2)

        xp_ratio = self.pokemon_player.xp / self.pokemon_player.xp_to_next_level
        fill_width = int(200*xp_ratio)
        if fill_width > 0:
            fill_rect = pygame.Rect(161, 161, fill_width, 7)
            pygame.draw.rect(self.window.screen, self.window.BLUE, fill_rect)

    def draw_stats(self):
        xp_text = self.window.text_font_battle.render(f"XP: {self.pokemon_player.xp}/{self.pokemon_player.xp_to_next_level} Level : {self.pokemon_player.level}", True, self.window.WHITE)
        self.window.screen.blit(xp_text, (160, 180))

    def start_fight(self):


        # draw background
        self.draw_background_fight()


        # draw pokemons
        self.pokemon_opponent[0].draw_pokemon_opponent_hp(self.pokemon_opponent[0])
        self.pokemon_player.draw_pokemon_player(self.pokemon_player)
        self.pokemon_opponent[0].draw_pokemon_opponent(self.pokemon_opponent[0])
        self.pokemon_player.draw_pokemon_player_hp(self.pokemon_player)
        self.draw_stats()
        self.draw_xp_bar()

        # draw bottom panel 
        self.draw_panel()
        self.select_menu_button_battle()




        # select action
        new_state = self.handle_events_battle()
        return new_state


    def draw_lose_buttons(self):
        """method to draw button on screen"""

        self.retry = self.window.create_text_image("Retry", self.window.text_font_menu, self.window.BLACK)
        self.return_to_menu = self.window.create_text_image("Return to menu", self.window.text_font_menu, self.window.BLACK)

        self.retry = Button(self.window.screen_middle_x-200,200,self.retry, self.window)
        self.return_to_menu = Button(self.window.screen_middle_x+100,200,self.return_to_menu, self.window)


        self.window.draw_text("You lose",self.window.text_font_menu_battle,self.window.RED,self.window.screen_middle_x-50,250)
        self.retry.draw_button()
        self.return_to_menu.draw_button()


    def select_menu_button_lose(self):
        """method to show which button is selected"""

        buttons_lose = (self.retry,self.return_to_menu)

        for position, button in enumerate(buttons_lose, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button, 3)


    def handle_events_lose(self):   
        """method to handle menu events"""

        buttons_lose = (self.retry,self.return_to_menu)
        total_lose_buttons = len(buttons_lose)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.selected_position = (self.selected_position % 2) +1 
                if event.key == K_LEFT:
                    self.selected_position = (self.selected_position - 2) % total_lose_buttons + 1 

                if event.key == K_RETURN:
                    if self.selected_position == 1 :
                        return "fight"  
                    else:
                        self.selected_position = 1
                        return "player_menu"
        return "lose_game"


    def lose_fight(self):

        # draw background
        self.draw_background_fight()
        self.draw_panel()

        # draw bottom panel 
        self.draw_lose_buttons()
        self.select_menu_button_lose()

        new_state = self.handle_events_lose()
        return new_state