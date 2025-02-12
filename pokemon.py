from window import Window
import pygame
import json
import random

with open("pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)


class Pokemon():
    """class to init pokemon, caract and draw"""

    def __init__(self):
        # background image
        self.window = Window()
        # pokemon 
        self.pokemon_id = 3
        self.pokemon_player = ""
        self.pokemon_opponent = ""
        self.pokemon_opponent_id = self.define_pokemon_opponent()
        self.pokemon_life = ""
        self.pokemon_name = ""

    # def define_pokemon_player(self):

    def define_pokemon_opponent(self):
        available_ids = [pokemon["pokedex_id"] for pokemon in data]
        # pokemon_opponent_id = random.choice(available_ids)
        # return pokemon_opponent_id
        return random.choice(available_ids)
    
    def get_name_opponent(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["name"]

    def get_hp_opponent(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["hp"]
            
    def draw_hp_opponent_pokemon(self):

        self.pokemon_name = self.get_name_opponent()
        self.pokemon_life = self.get_hp_opponent()
        
        self.window.draw_text(f"{self.pokemon_name} HP : {self.pokemon_life}",self.window.text_font_hp_opponent,self.window.WHITE,580,30)


    def draw_pokemons(self):
        """function to draw pokemon"""

        for pokemon in data:
            if pokemon["pokedex_id"]==self.pokemon_id:
                sprite_path = pokemon["sprites"]["back"]
                self.pokemon_player = pygame.image.load(sprite_path).convert_alpha()
                self.pokemon_player = pygame.transform.scale(self.pokemon_player, (self.pokemon_player.get_width()*3, self.pokemon_player.get_height()*3))
                break

        self.rect_pokemon_player = self.pokemon_player.get_rect()
        self.rect_pokemon_player.center = (250,330)
        self.window.screen.blit(self.pokemon_player,self.rect_pokemon_player)


        # self.pokemon_opponent_id = self.define_pokemon_opponent()
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                sprite_path_opponent = pokemon["sprites"]["front"]
                self.pokemon_opponent = pygame.image.load(sprite_path_opponent).convert_alpha()
                self.pokemon_opponent = pygame.transform.scale(self.pokemon_opponent, (self.pokemon_opponent.get_width()*3, self.pokemon_opponent.get_height()*3))
                break

        
        self.rect_pokemon_opponent = self.pokemon_opponent.get_rect()
        self.rect_pokemon_opponent.center = (650,160)
        self.window.screen.blit(self.pokemon_opponent,self.rect_pokemon_opponent)


    # def draw_life_pokemon(self):
