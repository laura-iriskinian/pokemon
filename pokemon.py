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
        self.pokemon_player = ""
        self.pokemon_player_id = 3
        self.pokemon_player_sprite = self.get_pokemon_player_sprite()

        self.pokemon_player_life = self.get_pokemon_player_hp()
        self.pokemon_player_name = self.get_pokemon_player_name()
        self.pokemon_player_type = self.get_pokemon_player_type()
        self.pokemon_player_def = self.get_pokemon_player_defense()
        self.pokemon_player_resistance = self.get_pokemon_player_resistance()
        self.pokemon_player_atk = self.get_pokemon_player_attack()


        # pokemon opponent
        self.pokemon_opponent = ""
        self.pokemon_opponent_id = self.get_pokemon_opponent_id()
        self.pokemon_opponent_sprite = self.get_pokemon_opponent_sprite()

        self.pokemon_opponent_life = self.get_pokemon_opponent_hp()
        self.pokemon_opponent_name = self.get_pokemon_opponent_name()
        self.pokemon_opponent_type = self.get_pokemon_opponent_type()
        self.pokemon_opponent_def = self.get_pokemon_opponent_defense()
        self.pokemon_opponent_resistance = self.get_pokemon_opponent_resistance()
        self.pokemon_opponent_atk = self.get_pokemon_opponent_attack()


# defs get players

    def get_pokemon_player_sprite(self):

        for pokemon in data:
            if pokemon["pokedex_id"]==self.pokemon_player_id:
                sprite_path = pokemon["sprites"]["back"]
                self.pokemon_player_sprite = pygame.image.load(sprite_path).convert_alpha()
                self.pokemon_player_sprite = pygame.transform.scale(self.pokemon_player_sprite, (self.pokemon_player_sprite.get_width()*3, self.pokemon_player_sprite.get_height()*3))
                return self.pokemon_player_sprite


    def get_pokemon_player_attack(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["atk"]

    def get_pokemon_player_name(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["name"]

    def get_pokemon_player_hp(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["hp"]

    def get_pokemon_player_defense(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["def"]
            
    def get_pokemon_player_resistance(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                for resistance in pokemon["resistances"]:
                    if resistance["name"] == self.pokemon_player_type:
                        return resistance["multiply"]
            
    def get_pokemon_player_type(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["type"]



# defs get opponent

    def get_pokemon_opponent_id(self):
        available_ids = [pokemon["pokedex_id"] for pokemon in data]
        return random.choice(available_ids)

    def get_pokemon_opponent_sprite(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                sprite_path_opponent = pokemon["sprites"]["front"]
                self.pokemon_opponent_sprite = pygame.image.load(sprite_path_opponent).convert_alpha()
                self.pokemon_opponent_sprite = pygame.transform.scale(self.pokemon_opponent_sprite, (self.pokemon_opponent_sprite.get_width()*3, self.pokemon_opponent_sprite.get_height()*3))
                return self.pokemon_opponent_sprite

    def get_pokemon_opponent_name(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["name"]

    def get_pokemon_opponent_hp(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["hp"]

    def get_pokemon_opponent_defense(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["def"]
            
    def get_pokemon_opponent_resistance(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                for resistance in pokemon["resistances"]:
                    if resistance["name"] == self.pokemon_opponent_type:
                        return resistance["multiply"]
            
    def get_pokemon_opponent_type(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["type"]

    def get_pokemon_opponent_attack(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["atk"]


# defs fight system :

    def player_attack(self):
        """the player attack the opponent"""
        resistance_multiplier = self.pokemon_opponent_resistance
        raw_damage = max(1,self.pokemon_player_atk - self.pokemon_opponent_def)
        damage = raw_damage * resistance_multiplier

        self.pokemon_opponent_life -= damage

    def opponent_attack(self):
        """the opponent attack the player"""
        resistance_multiplier = self.pokemon_player_resistance
        raw_damage = max(1,self.pokemon_opponent_atk - self.pokemon_player_def)
        damage = raw_damage * resistance_multiplier

        self.pokemon_player_life -= damage

    def draw_pokemon_opponent_hp(self):

        self.window.draw_text(f"{self.pokemon_opponent_name} HP : {self.pokemon_opponent_life}",
                            self.window.text_font_hp_opponent,
                            self.window.WHITE,560,25)
        
    def draw_pokemon_player_hp(self):

        self.window.draw_text(f"{self.pokemon_player_name} HP : {self.pokemon_player_life}",
                            self.window.text_font_hp_opponent,
                            self.window.WHITE,160,200)



    def draw_pokemon_player(self):
        """function to draw pokemon player"""

        # pokemon player
        self.rect_pokemon_player_sprite = self.pokemon_player_sprite.get_rect()
        self.rect_pokemon_player_sprite.center = (250,335)
        self.window.screen.blit(self.pokemon_player_sprite,self.rect_pokemon_player_sprite)

    def draw_pokemon_opponent(self):
        """function to draw pokemon opponent"""

        self.rect_pokemon_opponent_sprite = self.pokemon_opponent_sprite.get_rect()
        self.rect_pokemon_opponent_sprite.center = (650,160)
        self.window.screen.blit(self.pokemon_opponent_sprite,self.rect_pokemon_opponent_sprite)

    # def draw_life_pokemon(self):
