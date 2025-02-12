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
        pokemon_id = 3
        pokemon_player = None

        for pokemon in data:
            if pokemon["pokedex_id"]==pokemon_id:
                sprite_path = pokemon["sprites"]["back"]
                pokemon_player = pygame.image.load(sprite_path).convert_alpha()
                break
        
        self.pokemon_player = pygame.transform.scale(pokemon_player, (pokemon_player.get_width()*3, pokemon_player.get_height()*3))
        self.rect_pokemon_player = self.pokemon_player.get_rect()
        self.rect_pokemon_player.center = (250,330)
        
        available_ids = [pokemon["pokedex_id"] for pokemon in data]
        pokemon_opponent_id = random.choice(available_ids)
        pokemon_opponent = None

        for pokemon in data:
            if pokemon["pokedex_id"] == pokemon_opponent_id:
                sprite_path_opponent = pokemon["sprites"]["front"]
                pokemon_opponent = pygame.image.load(sprite_path_opponent).convert_alpha()
        self.pokemon_opponent = pygame.transform.scale(pokemon_opponent, (pokemon_opponent.get_width()*3, pokemon_opponent.get_height()*3))
        self.rect_pokemon_opponent = self.pokemon_opponent.get_rect()
        self.rect_pokemon_opponent.center = (650,160)


    def draw_pokemon(self):
        """function to draw pokemon"""
        self.window.screen.blit(self.pokemon_player,self.rect_pokemon_player)
        self.window.screen.blit(self.pokemon_opponent,self.rect_pokemon_opponent)